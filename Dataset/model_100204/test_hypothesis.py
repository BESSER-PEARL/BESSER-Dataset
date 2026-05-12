import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OrderBySpecification,
    QuerySearchCondition,
    query::Predicate,
    statements::SQLControlStatement,
    Procedure,
    MergeOperationSpecification,
    UpdateSource,
    query::OrderByOrdinal,
    statements::SQLDataChangeStatement,
    SQLObject,
    query::SQLQueryObject,
    Table,
    ValueExpressionCase,
    query::ValueExpressionCaseSearch,
    Grouping,
    query::SuperGroup,
    SuperGroupElement,
    query::SuperGroupElementExpression,
    query::SuperGroupElementSublist,
    GroupingSetsElement,
    query::GroupingSetsElementSublist,
    query::GroupingSetsElementExpression,
    GroupingSpecification,
    query::Grouping,
    query::GroupingSets,
    QueryValueExpression,
    query::ValueExpressionAtomic,
    Function,
    query::MergeInsertSpecification,
    ValueExpressionAtomic,
    query::ValueExpressionDefaultValue,
    query::ValueExpressionNullValue,
    query::ValueExpressionCase,
    query::ValueExpressionSimple,
    PredicateQuantified,
    PredicateIn,
    Predicate,
    query::PredicateQuantified,
    query::PredicateIn,
    query::OrderByResultColumn,
    QueryResultSpecification,
    query::ValueExpressionVariable,
    query::ResultTableAllColumns,
    TableReference,
    query::TableExpression,
    query::TableNested,
    QueryExpressionBody,
    query::QueryValues,
    query::ValueExpressionScalarSelect,
    query::ValueExpressionRow,
    query::UpdateSourceExprList,
    expressions::QueryExpression,
    query::ValueExpressionCaseSimple,
    query::ValueExpressionNested,
    query::ValueExpressionLabeledDuration,
    query::ValueExpressionCombined,
    query::ValueExpressionFunction,
    query::ValueExpressionCast,
    query::GroupingExpression,
    query::PredicateQuantifiedValueSelect,
    query::PredicateQuantifiedRowSelect,
    query::PredicateInValueSelect,
    query::PredicateInValueRowSelect,
    query::PredicateInValueList,
    query::PredicateBetween,
    query::PredicateLike,
    query::PredicateBasic,
    query::ResultColumn,
    query::OrderByValueExpression,
    query::PredicateIsNull,
    query::QueryNested,
    query::UpdateSourceQuery,
    query::PredicateExists,
    DataType,
    expressions::ValueExpression,
    TableExpression,
    query::TableFunction,
    query::TableQueryLateral,
    query::WithTableReference,
    query::QueryExpressionBody,
    query::SearchConditionNested,
    query::QuerySelect,
    query::QueryCombined,
    query::SearchConditionCombined,
    query::TableJoined,
    expressions::SearchCondition,
    query::MergeUpdateSpecification,
    QueryStatement,
    query::QueryChangeStatement,
    query::QuerySelectStatement,
    query::ValueExpressionColumn,
    query::TableInDatabase,
    statements::SQLDataStatement,
    SQLQueryObject,
    query::TableCorrelation,
    query::QueryExpressionRoot,
    query::UpdatabilityExpression,
    query::MergeOnCondition,
    query::ValueExpressionCaseElse,
    query::GroupingSpecification,
    query::QueryResultSpecification,
    query::CallStatement,
    query::UpdateOfColumn,
    query::ColumnName,
    query::ProcedureReference,
    query::SuperGroupElement,
    query::GroupingSetsElement,
    query::ValueExpressionCaseSimpleContent,
    query::ValuesRow,
    query::MergeOperationSpecification,
    query::UpdateAssignmentExpression,
    query::QuerySearchCondition,
    query::WithTableSpecification,
    query::ValueExpressionCaseSearchContent,
    query::TableReference,
    query::UpdateSource,
    query::CursorReference,
    query::MergeSourceTable,
    query::QueryValueExpression,
    query::OrderBySpecification,
    query::MergeTargetTable,
    query::QueryStatement,
    QueryChangeStatement,
    query::QueryMergeStatement,
    query::QueryUpdateStatement,
    query::QueryInsertStatement,
    query::QueryDeleteStatement,
    SuperGroupType,
    NullOrderingType,
    ValueExpressionLabeledDurationType,
    ValueExpressionUnaryOperator,
    OrderingSpecType,
    PredicateQuantifiedType,
    QueryCombinedOperator,
    UpdatabilityType,
    TableJoinedOperator,
    ValueExpressionCombinedOperator,
    SearchConditionCombinedOperator,
    PredicateComparisonOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_orderbyspecification_is_not_abstract():
    assert not inspect.isabstract(OrderBySpecification)


def test_orderbyspecification_constructor_exists():
    assert callable(OrderBySpecification.__init__)


def test_orderbyspecification_constructor_args():
    sig = inspect.signature(OrderBySpecification.__init__)
    params = list(sig.parameters.keys())



def test_querysearchcondition_is_not_abstract():
    assert not inspect.isabstract(QuerySearchCondition)


def test_querysearchcondition_constructor_exists():
    assert callable(QuerySearchCondition.__init__)


def test_querysearchcondition_constructor_args():
    sig = inspect.signature(QuerySearchCondition.__init__)
    params = list(sig.parameters.keys())



def test_query::predicate_is_not_abstract():
    assert not inspect.isabstract(query::Predicate)


def test_query::predicate_constructor_exists():
    assert callable(query::Predicate.__init__)


def test_query::predicate_constructor_args():
    sig = inspect.signature(query::Predicate.__init__)
    params = list(sig.parameters.keys())
    assert "negatedPredicate" in params, "Missing parameter 'negatedPredicate'"
    assert "hasSelectivity" in params, "Missing parameter 'hasSelectivity'"
    assert "selectivityValue" in params, "Missing parameter 'selectivityValue'"

def test_query::predicate_has_negatedPredicate():
    assert hasattr(query::Predicate, "negatedPredicate")
    descriptor = None
    for klass in query::Predicate.__mro__:
        if "negatedPredicate" in klass.__dict__:
            descriptor = klass.__dict__["negatedPredicate"]
            break
    assert isinstance(descriptor, property)

def test_query::predicate_has_hasSelectivity():
    assert hasattr(query::Predicate, "hasSelectivity")
    descriptor = None
    for klass in query::Predicate.__mro__:
        if "hasSelectivity" in klass.__dict__:
            descriptor = klass.__dict__["hasSelectivity"]
            break
    assert isinstance(descriptor, property)

def test_query::predicate_has_selectivityValue():
    assert hasattr(query::Predicate, "selectivityValue")
    descriptor = None
    for klass in query::Predicate.__mro__:
        if "selectivityValue" in klass.__dict__:
            descriptor = klass.__dict__["selectivityValue"]
            break
    assert isinstance(descriptor, property)



def test_statements::sqlcontrolstatement_is_not_abstract():
    assert not inspect.isabstract(statements::SQLControlStatement)


def test_statements::sqlcontrolstatement_constructor_exists():
    assert callable(statements::SQLControlStatement.__init__)


def test_statements::sqlcontrolstatement_constructor_args():
    sig = inspect.signature(statements::SQLControlStatement.__init__)
    params = list(sig.parameters.keys())



def test_procedure_is_not_abstract():
    assert not inspect.isabstract(Procedure)


def test_procedure_constructor_exists():
    assert callable(Procedure.__init__)


def test_procedure_constructor_args():
    sig = inspect.signature(Procedure.__init__)
    params = list(sig.parameters.keys())



def test_mergeoperationspecification_is_not_abstract():
    assert not inspect.isabstract(MergeOperationSpecification)


def test_mergeoperationspecification_constructor_exists():
    assert callable(MergeOperationSpecification.__init__)


def test_mergeoperationspecification_constructor_args():
    sig = inspect.signature(MergeOperationSpecification.__init__)
    params = list(sig.parameters.keys())



def test_updatesource_is_not_abstract():
    assert not inspect.isabstract(UpdateSource)


def test_updatesource_constructor_exists():
    assert callable(UpdateSource.__init__)


def test_updatesource_constructor_args():
    sig = inspect.signature(UpdateSource.__init__)
    params = list(sig.parameters.keys())



def test_query::orderbyordinal_is_not_abstract():
    assert not inspect.isabstract(query::OrderByOrdinal)


def test_query::orderbyordinal_constructor_exists():
    assert callable(query::OrderByOrdinal.__init__)


def test_query::orderbyordinal_constructor_args():
    sig = inspect.signature(query::OrderByOrdinal.__init__)
    params = list(sig.parameters.keys())
    assert "ordinalValue" in params, "Missing parameter 'ordinalValue'"

def test_query::orderbyordinal_has_ordinalValue():
    assert hasattr(query::OrderByOrdinal, "ordinalValue")
    descriptor = None
    for klass in query::OrderByOrdinal.__mro__:
        if "ordinalValue" in klass.__dict__:
            descriptor = klass.__dict__["ordinalValue"]
            break
    assert isinstance(descriptor, property)



def test_statements::sqldatachangestatement_is_not_abstract():
    assert not inspect.isabstract(statements::SQLDataChangeStatement)


def test_statements::sqldatachangestatement_constructor_exists():
    assert callable(statements::SQLDataChangeStatement.__init__)


def test_statements::sqldatachangestatement_constructor_args():
    sig = inspect.signature(statements::SQLDataChangeStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlobject_is_not_abstract():
    assert not inspect.isabstract(SQLObject)


def test_sqlobject_constructor_exists():
    assert callable(SQLObject.__init__)


def test_sqlobject_constructor_args():
    sig = inspect.signature(SQLObject.__init__)
    params = list(sig.parameters.keys())



def test_query::sqlqueryobject_is_not_abstract():
    assert not inspect.isabstract(query::SQLQueryObject)


def test_query::sqlqueryobject_constructor_exists():
    assert callable(query::SQLQueryObject.__init__)


def test_query::sqlqueryobject_constructor_args():
    sig = inspect.signature(query::SQLQueryObject.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_valueexpressioncase_is_not_abstract():
    assert not inspect.isabstract(ValueExpressionCase)


def test_valueexpressioncase_constructor_exists():
    assert callable(ValueExpressionCase.__init__)


def test_valueexpressioncase_constructor_args():
    sig = inspect.signature(ValueExpressionCase.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressioncasesearch_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionCaseSearch)


def test_query::valueexpressioncasesearch_constructor_exists():
    assert callable(query::ValueExpressionCaseSearch.__init__)


def test_query::valueexpressioncasesearch_constructor_args():
    sig = inspect.signature(query::ValueExpressionCaseSearch.__init__)
    params = list(sig.parameters.keys())



def test_grouping_is_not_abstract():
    assert not inspect.isabstract(Grouping)


def test_grouping_constructor_exists():
    assert callable(Grouping.__init__)


def test_grouping_constructor_args():
    sig = inspect.signature(Grouping.__init__)
    params = list(sig.parameters.keys())



def test_query::supergroup_is_not_abstract():
    assert not inspect.isabstract(query::SuperGroup)


def test_query::supergroup_constructor_exists():
    assert callable(query::SuperGroup.__init__)


def test_query::supergroup_constructor_args():
    sig = inspect.signature(query::SuperGroup.__init__)
    params = list(sig.parameters.keys())
    assert "superGroupType" in params, "Missing parameter 'superGroupType'"

def test_query::supergroup_has_superGroupType():
    assert hasattr(query::SuperGroup, "superGroupType")
    descriptor = None
    for klass in query::SuperGroup.__mro__:
        if "superGroupType" in klass.__dict__:
            descriptor = klass.__dict__["superGroupType"]
            break
    assert isinstance(descriptor, property)



def test_supergroupelement_is_not_abstract():
    assert not inspect.isabstract(SuperGroupElement)


def test_supergroupelement_constructor_exists():
    assert callable(SuperGroupElement.__init__)


def test_supergroupelement_constructor_args():
    sig = inspect.signature(SuperGroupElement.__init__)
    params = list(sig.parameters.keys())



def test_query::supergroupelementexpression_is_not_abstract():
    assert not inspect.isabstract(query::SuperGroupElementExpression)


def test_query::supergroupelementexpression_constructor_exists():
    assert callable(query::SuperGroupElementExpression.__init__)


def test_query::supergroupelementexpression_constructor_args():
    sig = inspect.signature(query::SuperGroupElementExpression.__init__)
    params = list(sig.parameters.keys())



def test_query::supergroupelementsublist_is_not_abstract():
    assert not inspect.isabstract(query::SuperGroupElementSublist)


def test_query::supergroupelementsublist_constructor_exists():
    assert callable(query::SuperGroupElementSublist.__init__)


def test_query::supergroupelementsublist_constructor_args():
    sig = inspect.signature(query::SuperGroupElementSublist.__init__)
    params = list(sig.parameters.keys())



def test_groupingsetselement_is_not_abstract():
    assert not inspect.isabstract(GroupingSetsElement)


def test_groupingsetselement_constructor_exists():
    assert callable(GroupingSetsElement.__init__)


def test_groupingsetselement_constructor_args():
    sig = inspect.signature(GroupingSetsElement.__init__)
    params = list(sig.parameters.keys())



def test_query::groupingsetselementsublist_is_not_abstract():
    assert not inspect.isabstract(query::GroupingSetsElementSublist)


def test_query::groupingsetselementsublist_constructor_exists():
    assert callable(query::GroupingSetsElementSublist.__init__)


def test_query::groupingsetselementsublist_constructor_args():
    sig = inspect.signature(query::GroupingSetsElementSublist.__init__)
    params = list(sig.parameters.keys())



def test_query::groupingsetselementexpression_is_not_abstract():
    assert not inspect.isabstract(query::GroupingSetsElementExpression)


def test_query::groupingsetselementexpression_constructor_exists():
    assert callable(query::GroupingSetsElementExpression.__init__)


def test_query::groupingsetselementexpression_constructor_args():
    sig = inspect.signature(query::GroupingSetsElementExpression.__init__)
    params = list(sig.parameters.keys())



def test_groupingspecification_is_not_abstract():
    assert not inspect.isabstract(GroupingSpecification)


def test_groupingspecification_constructor_exists():
    assert callable(GroupingSpecification.__init__)


def test_groupingspecification_constructor_args():
    sig = inspect.signature(GroupingSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query::grouping_is_not_abstract():
    assert not inspect.isabstract(query::Grouping)


def test_query::grouping_constructor_exists():
    assert callable(query::Grouping.__init__)


def test_query::grouping_constructor_args():
    sig = inspect.signature(query::Grouping.__init__)
    params = list(sig.parameters.keys())



def test_query::groupingsets_is_not_abstract():
    assert not inspect.isabstract(query::GroupingSets)


def test_query::groupingsets_constructor_exists():
    assert callable(query::GroupingSets.__init__)


def test_query::groupingsets_constructor_args():
    sig = inspect.signature(query::GroupingSets.__init__)
    params = list(sig.parameters.keys())



def test_queryvalueexpression_is_not_abstract():
    assert not inspect.isabstract(QueryValueExpression)


def test_queryvalueexpression_constructor_exists():
    assert callable(QueryValueExpression.__init__)


def test_queryvalueexpression_constructor_args():
    sig = inspect.signature(QueryValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressionatomic_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionAtomic)


def test_query::valueexpressionatomic_constructor_exists():
    assert callable(query::ValueExpressionAtomic.__init__)


def test_query::valueexpressionatomic_constructor_args():
    sig = inspect.signature(query::ValueExpressionAtomic.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_query::mergeinsertspecification_is_not_abstract():
    assert not inspect.isabstract(query::MergeInsertSpecification)


def test_query::mergeinsertspecification_constructor_exists():
    assert callable(query::MergeInsertSpecification.__init__)


def test_query::mergeinsertspecification_constructor_args():
    sig = inspect.signature(query::MergeInsertSpecification.__init__)
    params = list(sig.parameters.keys())



def test_valueexpressionatomic_is_not_abstract():
    assert not inspect.isabstract(ValueExpressionAtomic)


def test_valueexpressionatomic_constructor_exists():
    assert callable(ValueExpressionAtomic.__init__)


def test_valueexpressionatomic_constructor_args():
    sig = inspect.signature(ValueExpressionAtomic.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressiondefaultvalue_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionDefaultValue)


def test_query::valueexpressiondefaultvalue_constructor_exists():
    assert callable(query::ValueExpressionDefaultValue.__init__)


def test_query::valueexpressiondefaultvalue_constructor_args():
    sig = inspect.signature(query::ValueExpressionDefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressionnullvalue_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionNullValue)


def test_query::valueexpressionnullvalue_constructor_exists():
    assert callable(query::ValueExpressionNullValue.__init__)


def test_query::valueexpressionnullvalue_constructor_args():
    sig = inspect.signature(query::ValueExpressionNullValue.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressioncase_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionCase)


def test_query::valueexpressioncase_constructor_exists():
    assert callable(query::ValueExpressionCase.__init__)


def test_query::valueexpressioncase_constructor_args():
    sig = inspect.signature(query::ValueExpressionCase.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressionsimple_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionSimple)


def test_query::valueexpressionsimple_constructor_exists():
    assert callable(query::ValueExpressionSimple.__init__)


def test_query::valueexpressionsimple_constructor_args():
    sig = inspect.signature(query::ValueExpressionSimple.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_query::valueexpressionsimple_has_value():
    assert hasattr(query::ValueExpressionSimple, "value")
    descriptor = None
    for klass in query::ValueExpressionSimple.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_predicatequantified_is_not_abstract():
    assert not inspect.isabstract(PredicateQuantified)


def test_predicatequantified_constructor_exists():
    assert callable(PredicateQuantified.__init__)


def test_predicatequantified_constructor_args():
    sig = inspect.signature(PredicateQuantified.__init__)
    params = list(sig.parameters.keys())



def test_predicatein_is_not_abstract():
    assert not inspect.isabstract(PredicateIn)


def test_predicatein_constructor_exists():
    assert callable(PredicateIn.__init__)


def test_predicatein_constructor_args():
    sig = inspect.signature(PredicateIn.__init__)
    params = list(sig.parameters.keys())



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_query::predicatequantified_is_not_abstract():
    assert not inspect.isabstract(query::PredicateQuantified)


def test_query::predicatequantified_constructor_exists():
    assert callable(query::PredicateQuantified.__init__)


def test_query::predicatequantified_constructor_args():
    sig = inspect.signature(query::PredicateQuantified.__init__)
    params = list(sig.parameters.keys())



def test_query::predicatein_is_not_abstract():
    assert not inspect.isabstract(query::PredicateIn)


def test_query::predicatein_constructor_exists():
    assert callable(query::PredicateIn.__init__)


def test_query::predicatein_constructor_args():
    sig = inspect.signature(query::PredicateIn.__init__)
    params = list(sig.parameters.keys())
    assert "notIn" in params, "Missing parameter 'notIn'"

def test_query::predicatein_has_notIn():
    assert hasattr(query::PredicateIn, "notIn")
    descriptor = None
    for klass in query::PredicateIn.__mro__:
        if "notIn" in klass.__dict__:
            descriptor = klass.__dict__["notIn"]
            break
    assert isinstance(descriptor, property)



def test_query::orderbyresultcolumn_is_not_abstract():
    assert not inspect.isabstract(query::OrderByResultColumn)


def test_query::orderbyresultcolumn_constructor_exists():
    assert callable(query::OrderByResultColumn.__init__)


def test_query::orderbyresultcolumn_constructor_args():
    sig = inspect.signature(query::OrderByResultColumn.__init__)
    params = list(sig.parameters.keys())



def test_queryresultspecification_is_not_abstract():
    assert not inspect.isabstract(QueryResultSpecification)


def test_queryresultspecification_constructor_exists():
    assert callable(QueryResultSpecification.__init__)


def test_queryresultspecification_constructor_args():
    sig = inspect.signature(QueryResultSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressionvariable_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionVariable)


def test_query::valueexpressionvariable_constructor_exists():
    assert callable(query::ValueExpressionVariable.__init__)


def test_query::valueexpressionvariable_constructor_args():
    sig = inspect.signature(query::ValueExpressionVariable.__init__)
    params = list(sig.parameters.keys())



def test_query::resulttableallcolumns_is_not_abstract():
    assert not inspect.isabstract(query::ResultTableAllColumns)


def test_query::resulttableallcolumns_constructor_exists():
    assert callable(query::ResultTableAllColumns.__init__)


def test_query::resulttableallcolumns_constructor_args():
    sig = inspect.signature(query::ResultTableAllColumns.__init__)
    params = list(sig.parameters.keys())



def test_tablereference_is_not_abstract():
    assert not inspect.isabstract(TableReference)


def test_tablereference_constructor_exists():
    assert callable(TableReference.__init__)


def test_tablereference_constructor_args():
    sig = inspect.signature(TableReference.__init__)
    params = list(sig.parameters.keys())



def test_query::tableexpression_is_not_abstract():
    assert not inspect.isabstract(query::TableExpression)


def test_query::tableexpression_constructor_exists():
    assert callable(query::TableExpression.__init__)


def test_query::tableexpression_constructor_args():
    sig = inspect.signature(query::TableExpression.__init__)
    params = list(sig.parameters.keys())



def test_query::tablenested_is_not_abstract():
    assert not inspect.isabstract(query::TableNested)


def test_query::tablenested_constructor_exists():
    assert callable(query::TableNested.__init__)


def test_query::tablenested_constructor_args():
    sig = inspect.signature(query::TableNested.__init__)
    params = list(sig.parameters.keys())



def test_queryexpressionbody_is_not_abstract():
    assert not inspect.isabstract(QueryExpressionBody)


def test_queryexpressionbody_constructor_exists():
    assert callable(QueryExpressionBody.__init__)


def test_queryexpressionbody_constructor_args():
    sig = inspect.signature(QueryExpressionBody.__init__)
    params = list(sig.parameters.keys())



def test_query::queryvalues_is_not_abstract():
    assert not inspect.isabstract(query::QueryValues)


def test_query::queryvalues_constructor_exists():
    assert callable(query::QueryValues.__init__)


def test_query::queryvalues_constructor_args():
    sig = inspect.signature(query::QueryValues.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressionscalarselect_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionScalarSelect)


def test_query::valueexpressionscalarselect_constructor_exists():
    assert callable(query::ValueExpressionScalarSelect.__init__)


def test_query::valueexpressionscalarselect_constructor_args():
    sig = inspect.signature(query::ValueExpressionScalarSelect.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressionrow_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionRow)


def test_query::valueexpressionrow_constructor_exists():
    assert callable(query::ValueExpressionRow.__init__)


def test_query::valueexpressionrow_constructor_args():
    sig = inspect.signature(query::ValueExpressionRow.__init__)
    params = list(sig.parameters.keys())



def test_query::updatesourceexprlist_is_not_abstract():
    assert not inspect.isabstract(query::UpdateSourceExprList)


def test_query::updatesourceexprlist_constructor_exists():
    assert callable(query::UpdateSourceExprList.__init__)


def test_query::updatesourceexprlist_constructor_args():
    sig = inspect.signature(query::UpdateSourceExprList.__init__)
    params = list(sig.parameters.keys())



def test_expressions::queryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::QueryExpression)


def test_expressions::queryexpression_constructor_exists():
    assert callable(expressions::QueryExpression.__init__)


def test_expressions::queryexpression_constructor_args():
    sig = inspect.signature(expressions::QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressioncasesimple_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionCaseSimple)


def test_query::valueexpressioncasesimple_constructor_exists():
    assert callable(query::ValueExpressionCaseSimple.__init__)


def test_query::valueexpressioncasesimple_constructor_args():
    sig = inspect.signature(query::ValueExpressionCaseSimple.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressionnested_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionNested)


def test_query::valueexpressionnested_constructor_exists():
    assert callable(query::ValueExpressionNested.__init__)


def test_query::valueexpressionnested_constructor_args():
    sig = inspect.signature(query::ValueExpressionNested.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressionlabeledduration_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionLabeledDuration)


def test_query::valueexpressionlabeledduration_constructor_exists():
    assert callable(query::ValueExpressionLabeledDuration.__init__)


def test_query::valueexpressionlabeledduration_constructor_args():
    sig = inspect.signature(query::ValueExpressionLabeledDuration.__init__)
    params = list(sig.parameters.keys())
    assert "labeledDurationType" in params, "Missing parameter 'labeledDurationType'"

def test_query::valueexpressionlabeledduration_has_labeledDurationType():
    assert hasattr(query::ValueExpressionLabeledDuration, "labeledDurationType")
    descriptor = None
    for klass in query::ValueExpressionLabeledDuration.__mro__:
        if "labeledDurationType" in klass.__dict__:
            descriptor = klass.__dict__["labeledDurationType"]
            break
    assert isinstance(descriptor, property)



def test_query::valueexpressioncombined_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionCombined)


def test_query::valueexpressioncombined_constructor_exists():
    assert callable(query::ValueExpressionCombined.__init__)


def test_query::valueexpressioncombined_constructor_args():
    sig = inspect.signature(query::ValueExpressionCombined.__init__)
    params = list(sig.parameters.keys())
    assert "combinedOperator" in params, "Missing parameter 'combinedOperator'"

def test_query::valueexpressioncombined_has_combinedOperator():
    assert hasattr(query::ValueExpressionCombined, "combinedOperator")
    descriptor = None
    for klass in query::ValueExpressionCombined.__mro__:
        if "combinedOperator" in klass.__dict__:
            descriptor = klass.__dict__["combinedOperator"]
            break
    assert isinstance(descriptor, property)



def test_query::valueexpressionfunction_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionFunction)


def test_query::valueexpressionfunction_constructor_exists():
    assert callable(query::ValueExpressionFunction.__init__)


def test_query::valueexpressionfunction_constructor_args():
    sig = inspect.signature(query::ValueExpressionFunction.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"
    assert "columnFunction" in params, "Missing parameter 'columnFunction'"
    assert "specialRegister" in params, "Missing parameter 'specialRegister'"

def test_query::valueexpressionfunction_has_distinct():
    assert hasattr(query::ValueExpressionFunction, "distinct")
    descriptor = None
    for klass in query::ValueExpressionFunction.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)

def test_query::valueexpressionfunction_has_columnFunction():
    assert hasattr(query::ValueExpressionFunction, "columnFunction")
    descriptor = None
    for klass in query::ValueExpressionFunction.__mro__:
        if "columnFunction" in klass.__dict__:
            descriptor = klass.__dict__["columnFunction"]
            break
    assert isinstance(descriptor, property)

def test_query::valueexpressionfunction_has_specialRegister():
    assert hasattr(query::ValueExpressionFunction, "specialRegister")
    descriptor = None
    for klass in query::ValueExpressionFunction.__mro__:
        if "specialRegister" in klass.__dict__:
            descriptor = klass.__dict__["specialRegister"]
            break
    assert isinstance(descriptor, property)



def test_query::valueexpressioncast_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionCast)


def test_query::valueexpressioncast_constructor_exists():
    assert callable(query::ValueExpressionCast.__init__)


def test_query::valueexpressioncast_constructor_args():
    sig = inspect.signature(query::ValueExpressionCast.__init__)
    params = list(sig.parameters.keys())



def test_query::groupingexpression_is_not_abstract():
    assert not inspect.isabstract(query::GroupingExpression)


def test_query::groupingexpression_constructor_exists():
    assert callable(query::GroupingExpression.__init__)


def test_query::groupingexpression_constructor_args():
    sig = inspect.signature(query::GroupingExpression.__init__)
    params = list(sig.parameters.keys())



def test_query::predicatequantifiedvalueselect_is_not_abstract():
    assert not inspect.isabstract(query::PredicateQuantifiedValueSelect)


def test_query::predicatequantifiedvalueselect_constructor_exists():
    assert callable(query::PredicateQuantifiedValueSelect.__init__)


def test_query::predicatequantifiedvalueselect_constructor_args():
    sig = inspect.signature(query::PredicateQuantifiedValueSelect.__init__)
    params = list(sig.parameters.keys())
    assert "quantifiedType" in params, "Missing parameter 'quantifiedType'"
    assert "comparisonOperator" in params, "Missing parameter 'comparisonOperator'"

def test_query::predicatequantifiedvalueselect_has_quantifiedType():
    assert hasattr(query::PredicateQuantifiedValueSelect, "quantifiedType")
    descriptor = None
    for klass in query::PredicateQuantifiedValueSelect.__mro__:
        if "quantifiedType" in klass.__dict__:
            descriptor = klass.__dict__["quantifiedType"]
            break
    assert isinstance(descriptor, property)

def test_query::predicatequantifiedvalueselect_has_comparisonOperator():
    assert hasattr(query::PredicateQuantifiedValueSelect, "comparisonOperator")
    descriptor = None
    for klass in query::PredicateQuantifiedValueSelect.__mro__:
        if "comparisonOperator" in klass.__dict__:
            descriptor = klass.__dict__["comparisonOperator"]
            break
    assert isinstance(descriptor, property)



def test_query::predicatequantifiedrowselect_is_not_abstract():
    assert not inspect.isabstract(query::PredicateQuantifiedRowSelect)


def test_query::predicatequantifiedrowselect_constructor_exists():
    assert callable(query::PredicateQuantifiedRowSelect.__init__)


def test_query::predicatequantifiedrowselect_constructor_args():
    sig = inspect.signature(query::PredicateQuantifiedRowSelect.__init__)
    params = list(sig.parameters.keys())
    assert "quantifiedType" in params, "Missing parameter 'quantifiedType'"

def test_query::predicatequantifiedrowselect_has_quantifiedType():
    assert hasattr(query::PredicateQuantifiedRowSelect, "quantifiedType")
    descriptor = None
    for klass in query::PredicateQuantifiedRowSelect.__mro__:
        if "quantifiedType" in klass.__dict__:
            descriptor = klass.__dict__["quantifiedType"]
            break
    assert isinstance(descriptor, property)



def test_query::predicateinvalueselect_is_not_abstract():
    assert not inspect.isabstract(query::PredicateInValueSelect)


def test_query::predicateinvalueselect_constructor_exists():
    assert callable(query::PredicateInValueSelect.__init__)


def test_query::predicateinvalueselect_constructor_args():
    sig = inspect.signature(query::PredicateInValueSelect.__init__)
    params = list(sig.parameters.keys())



def test_query::predicateinvaluerowselect_is_not_abstract():
    assert not inspect.isabstract(query::PredicateInValueRowSelect)


def test_query::predicateinvaluerowselect_constructor_exists():
    assert callable(query::PredicateInValueRowSelect.__init__)


def test_query::predicateinvaluerowselect_constructor_args():
    sig = inspect.signature(query::PredicateInValueRowSelect.__init__)
    params = list(sig.parameters.keys())



def test_query::predicateinvaluelist_is_not_abstract():
    assert not inspect.isabstract(query::PredicateInValueList)


def test_query::predicateinvaluelist_constructor_exists():
    assert callable(query::PredicateInValueList.__init__)


def test_query::predicateinvaluelist_constructor_args():
    sig = inspect.signature(query::PredicateInValueList.__init__)
    params = list(sig.parameters.keys())



def test_query::predicatebetween_is_not_abstract():
    assert not inspect.isabstract(query::PredicateBetween)


def test_query::predicatebetween_constructor_exists():
    assert callable(query::PredicateBetween.__init__)


def test_query::predicatebetween_constructor_args():
    sig = inspect.signature(query::PredicateBetween.__init__)
    params = list(sig.parameters.keys())
    assert "notBetween" in params, "Missing parameter 'notBetween'"

def test_query::predicatebetween_has_notBetween():
    assert hasattr(query::PredicateBetween, "notBetween")
    descriptor = None
    for klass in query::PredicateBetween.__mro__:
        if "notBetween" in klass.__dict__:
            descriptor = klass.__dict__["notBetween"]
            break
    assert isinstance(descriptor, property)



def test_query::predicatelike_is_not_abstract():
    assert not inspect.isabstract(query::PredicateLike)


def test_query::predicatelike_constructor_exists():
    assert callable(query::PredicateLike.__init__)


def test_query::predicatelike_constructor_args():
    sig = inspect.signature(query::PredicateLike.__init__)
    params = list(sig.parameters.keys())
    assert "notLike" in params, "Missing parameter 'notLike'"

def test_query::predicatelike_has_notLike():
    assert hasattr(query::PredicateLike, "notLike")
    descriptor = None
    for klass in query::PredicateLike.__mro__:
        if "notLike" in klass.__dict__:
            descriptor = klass.__dict__["notLike"]
            break
    assert isinstance(descriptor, property)



def test_query::predicatebasic_is_not_abstract():
    assert not inspect.isabstract(query::PredicateBasic)


def test_query::predicatebasic_constructor_exists():
    assert callable(query::PredicateBasic.__init__)


def test_query::predicatebasic_constructor_args():
    sig = inspect.signature(query::PredicateBasic.__init__)
    params = list(sig.parameters.keys())
    assert "comparisonOperator" in params, "Missing parameter 'comparisonOperator'"

def test_query::predicatebasic_has_comparisonOperator():
    assert hasattr(query::PredicateBasic, "comparisonOperator")
    descriptor = None
    for klass in query::PredicateBasic.__mro__:
        if "comparisonOperator" in klass.__dict__:
            descriptor = klass.__dict__["comparisonOperator"]
            break
    assert isinstance(descriptor, property)



def test_query::resultcolumn_is_not_abstract():
    assert not inspect.isabstract(query::ResultColumn)


def test_query::resultcolumn_constructor_exists():
    assert callable(query::ResultColumn.__init__)


def test_query::resultcolumn_constructor_args():
    sig = inspect.signature(query::ResultColumn.__init__)
    params = list(sig.parameters.keys())



def test_query::orderbyvalueexpression_is_not_abstract():
    assert not inspect.isabstract(query::OrderByValueExpression)


def test_query::orderbyvalueexpression_constructor_exists():
    assert callable(query::OrderByValueExpression.__init__)


def test_query::orderbyvalueexpression_constructor_args():
    sig = inspect.signature(query::OrderByValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_query::predicateisnull_is_not_abstract():
    assert not inspect.isabstract(query::PredicateIsNull)


def test_query::predicateisnull_constructor_exists():
    assert callable(query::PredicateIsNull.__init__)


def test_query::predicateisnull_constructor_args():
    sig = inspect.signature(query::PredicateIsNull.__init__)
    params = list(sig.parameters.keys())
    assert "notNull" in params, "Missing parameter 'notNull'"

def test_query::predicateisnull_has_notNull():
    assert hasattr(query::PredicateIsNull, "notNull")
    descriptor = None
    for klass in query::PredicateIsNull.__mro__:
        if "notNull" in klass.__dict__:
            descriptor = klass.__dict__["notNull"]
            break
    assert isinstance(descriptor, property)



def test_query::querynested_is_not_abstract():
    assert not inspect.isabstract(query::QueryNested)


def test_query::querynested_constructor_exists():
    assert callable(query::QueryNested.__init__)


def test_query::querynested_constructor_args():
    sig = inspect.signature(query::QueryNested.__init__)
    params = list(sig.parameters.keys())



def test_query::updatesourcequery_is_not_abstract():
    assert not inspect.isabstract(query::UpdateSourceQuery)


def test_query::updatesourcequery_constructor_exists():
    assert callable(query::UpdateSourceQuery.__init__)


def test_query::updatesourcequery_constructor_args():
    sig = inspect.signature(query::UpdateSourceQuery.__init__)
    params = list(sig.parameters.keys())



def test_query::predicateexists_is_not_abstract():
    assert not inspect.isabstract(query::PredicateExists)


def test_query::predicateexists_constructor_exists():
    assert callable(query::PredicateExists.__init__)


def test_query::predicateexists_constructor_args():
    sig = inspect.signature(query::PredicateExists.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_expressions::valueexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::ValueExpression)


def test_expressions::valueexpression_constructor_exists():
    assert callable(expressions::ValueExpression.__init__)


def test_expressions::valueexpression_constructor_args():
    sig = inspect.signature(expressions::ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_tableexpression_is_not_abstract():
    assert not inspect.isabstract(TableExpression)


def test_tableexpression_constructor_exists():
    assert callable(TableExpression.__init__)


def test_tableexpression_constructor_args():
    sig = inspect.signature(TableExpression.__init__)
    params = list(sig.parameters.keys())



def test_query::tablefunction_is_not_abstract():
    assert not inspect.isabstract(query::TableFunction)


def test_query::tablefunction_constructor_exists():
    assert callable(query::TableFunction.__init__)


def test_query::tablefunction_constructor_args():
    sig = inspect.signature(query::TableFunction.__init__)
    params = list(sig.parameters.keys())



def test_query::tablequerylateral_is_not_abstract():
    assert not inspect.isabstract(query::TableQueryLateral)


def test_query::tablequerylateral_constructor_exists():
    assert callable(query::TableQueryLateral.__init__)


def test_query::tablequerylateral_constructor_args():
    sig = inspect.signature(query::TableQueryLateral.__init__)
    params = list(sig.parameters.keys())



def test_query::withtablereference_is_not_abstract():
    assert not inspect.isabstract(query::WithTableReference)


def test_query::withtablereference_constructor_exists():
    assert callable(query::WithTableReference.__init__)


def test_query::withtablereference_constructor_args():
    sig = inspect.signature(query::WithTableReference.__init__)
    params = list(sig.parameters.keys())



def test_query::queryexpressionbody_is_not_abstract():
    assert not inspect.isabstract(query::QueryExpressionBody)


def test_query::queryexpressionbody_constructor_exists():
    assert callable(query::QueryExpressionBody.__init__)


def test_query::queryexpressionbody_constructor_args():
    sig = inspect.signature(query::QueryExpressionBody.__init__)
    params = list(sig.parameters.keys())
    assert "rowFetchLimit" in params, "Missing parameter 'rowFetchLimit'"

def test_query::queryexpressionbody_has_rowFetchLimit():
    assert hasattr(query::QueryExpressionBody, "rowFetchLimit")
    descriptor = None
    for klass in query::QueryExpressionBody.__mro__:
        if "rowFetchLimit" in klass.__dict__:
            descriptor = klass.__dict__["rowFetchLimit"]
            break
    assert isinstance(descriptor, property)



def test_query::searchconditionnested_is_not_abstract():
    assert not inspect.isabstract(query::SearchConditionNested)


def test_query::searchconditionnested_constructor_exists():
    assert callable(query::SearchConditionNested.__init__)


def test_query::searchconditionnested_constructor_args():
    sig = inspect.signature(query::SearchConditionNested.__init__)
    params = list(sig.parameters.keys())



def test_query::queryselect_is_not_abstract():
    assert not inspect.isabstract(query::QuerySelect)


def test_query::queryselect_constructor_exists():
    assert callable(query::QuerySelect.__init__)


def test_query::queryselect_constructor_args():
    sig = inspect.signature(query::QuerySelect.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_query::queryselect_has_distinct():
    assert hasattr(query::QuerySelect, "distinct")
    descriptor = None
    for klass in query::QuerySelect.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_query::querycombined_is_not_abstract():
    assert not inspect.isabstract(query::QueryCombined)


def test_query::querycombined_constructor_exists():
    assert callable(query::QueryCombined.__init__)


def test_query::querycombined_constructor_args():
    sig = inspect.signature(query::QueryCombined.__init__)
    params = list(sig.parameters.keys())
    assert "combinedOperator" in params, "Missing parameter 'combinedOperator'"

def test_query::querycombined_has_combinedOperator():
    assert hasattr(query::QueryCombined, "combinedOperator")
    descriptor = None
    for klass in query::QueryCombined.__mro__:
        if "combinedOperator" in klass.__dict__:
            descriptor = klass.__dict__["combinedOperator"]
            break
    assert isinstance(descriptor, property)



def test_query::searchconditioncombined_is_not_abstract():
    assert not inspect.isabstract(query::SearchConditionCombined)


def test_query::searchconditioncombined_constructor_exists():
    assert callable(query::SearchConditionCombined.__init__)


def test_query::searchconditioncombined_constructor_args():
    sig = inspect.signature(query::SearchConditionCombined.__init__)
    params = list(sig.parameters.keys())
    assert "combinedOperator" in params, "Missing parameter 'combinedOperator'"

def test_query::searchconditioncombined_has_combinedOperator():
    assert hasattr(query::SearchConditionCombined, "combinedOperator")
    descriptor = None
    for klass in query::SearchConditionCombined.__mro__:
        if "combinedOperator" in klass.__dict__:
            descriptor = klass.__dict__["combinedOperator"]
            break
    assert isinstance(descriptor, property)



def test_query::tablejoined_is_not_abstract():
    assert not inspect.isabstract(query::TableJoined)


def test_query::tablejoined_constructor_exists():
    assert callable(query::TableJoined.__init__)


def test_query::tablejoined_constructor_args():
    sig = inspect.signature(query::TableJoined.__init__)
    params = list(sig.parameters.keys())
    assert "joinOperator" in params, "Missing parameter 'joinOperator'"

def test_query::tablejoined_has_joinOperator():
    assert hasattr(query::TableJoined, "joinOperator")
    descriptor = None
    for klass in query::TableJoined.__mro__:
        if "joinOperator" in klass.__dict__:
            descriptor = klass.__dict__["joinOperator"]
            break
    assert isinstance(descriptor, property)



def test_expressions::searchcondition_is_not_abstract():
    assert not inspect.isabstract(expressions::SearchCondition)


def test_expressions::searchcondition_constructor_exists():
    assert callable(expressions::SearchCondition.__init__)


def test_expressions::searchcondition_constructor_args():
    sig = inspect.signature(expressions::SearchCondition.__init__)
    params = list(sig.parameters.keys())



def test_query::mergeupdatespecification_is_not_abstract():
    assert not inspect.isabstract(query::MergeUpdateSpecification)


def test_query::mergeupdatespecification_constructor_exists():
    assert callable(query::MergeUpdateSpecification.__init__)


def test_query::mergeupdatespecification_constructor_args():
    sig = inspect.signature(query::MergeUpdateSpecification.__init__)
    params = list(sig.parameters.keys())



def test_querystatement_is_not_abstract():
    assert not inspect.isabstract(QueryStatement)


def test_querystatement_constructor_exists():
    assert callable(QueryStatement.__init__)


def test_querystatement_constructor_args():
    sig = inspect.signature(QueryStatement.__init__)
    params = list(sig.parameters.keys())



def test_query::querychangestatement_is_not_abstract():
    assert not inspect.isabstract(query::QueryChangeStatement)


def test_query::querychangestatement_constructor_exists():
    assert callable(query::QueryChangeStatement.__init__)


def test_query::querychangestatement_constructor_args():
    sig = inspect.signature(query::QueryChangeStatement.__init__)
    params = list(sig.parameters.keys())



def test_query::queryselectstatement_is_not_abstract():
    assert not inspect.isabstract(query::QuerySelectStatement)


def test_query::queryselectstatement_constructor_exists():
    assert callable(query::QuerySelectStatement.__init__)


def test_query::queryselectstatement_constructor_args():
    sig = inspect.signature(query::QuerySelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressioncolumn_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionColumn)


def test_query::valueexpressioncolumn_constructor_exists():
    assert callable(query::ValueExpressionColumn.__init__)


def test_query::valueexpressioncolumn_constructor_args():
    sig = inspect.signature(query::ValueExpressionColumn.__init__)
    params = list(sig.parameters.keys())



def test_query::tableindatabase_is_not_abstract():
    assert not inspect.isabstract(query::TableInDatabase)


def test_query::tableindatabase_constructor_exists():
    assert callable(query::TableInDatabase.__init__)


def test_query::tableindatabase_constructor_args():
    sig = inspect.signature(query::TableInDatabase.__init__)
    params = list(sig.parameters.keys())



def test_statements::sqldatastatement_is_not_abstract():
    assert not inspect.isabstract(statements::SQLDataStatement)


def test_statements::sqldatastatement_constructor_exists():
    assert callable(statements::SQLDataStatement.__init__)


def test_statements::sqldatastatement_constructor_args():
    sig = inspect.signature(statements::SQLDataStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlqueryobject_is_not_abstract():
    assert not inspect.isabstract(SQLQueryObject)


def test_sqlqueryobject_constructor_exists():
    assert callable(SQLQueryObject.__init__)


def test_sqlqueryobject_constructor_args():
    sig = inspect.signature(SQLQueryObject.__init__)
    params = list(sig.parameters.keys())



def test_query::tablecorrelation_is_not_abstract():
    assert not inspect.isabstract(query::TableCorrelation)


def test_query::tablecorrelation_constructor_exists():
    assert callable(query::TableCorrelation.__init__)


def test_query::tablecorrelation_constructor_args():
    sig = inspect.signature(query::TableCorrelation.__init__)
    params = list(sig.parameters.keys())



def test_query::queryexpressionroot_is_not_abstract():
    assert not inspect.isabstract(query::QueryExpressionRoot)


def test_query::queryexpressionroot_constructor_exists():
    assert callable(query::QueryExpressionRoot.__init__)


def test_query::queryexpressionroot_constructor_args():
    sig = inspect.signature(query::QueryExpressionRoot.__init__)
    params = list(sig.parameters.keys())



def test_query::updatabilityexpression_is_not_abstract():
    assert not inspect.isabstract(query::UpdatabilityExpression)


def test_query::updatabilityexpression_constructor_exists():
    assert callable(query::UpdatabilityExpression.__init__)


def test_query::updatabilityexpression_constructor_args():
    sig = inspect.signature(query::UpdatabilityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "updatabilityType" in params, "Missing parameter 'updatabilityType'"

def test_query::updatabilityexpression_has_updatabilityType():
    assert hasattr(query::UpdatabilityExpression, "updatabilityType")
    descriptor = None
    for klass in query::UpdatabilityExpression.__mro__:
        if "updatabilityType" in klass.__dict__:
            descriptor = klass.__dict__["updatabilityType"]
            break
    assert isinstance(descriptor, property)



def test_query::mergeoncondition_is_not_abstract():
    assert not inspect.isabstract(query::MergeOnCondition)


def test_query::mergeoncondition_constructor_exists():
    assert callable(query::MergeOnCondition.__init__)


def test_query::mergeoncondition_constructor_args():
    sig = inspect.signature(query::MergeOnCondition.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressioncaseelse_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionCaseElse)


def test_query::valueexpressioncaseelse_constructor_exists():
    assert callable(query::ValueExpressionCaseElse.__init__)


def test_query::valueexpressioncaseelse_constructor_args():
    sig = inspect.signature(query::ValueExpressionCaseElse.__init__)
    params = list(sig.parameters.keys())



def test_query::groupingspecification_is_not_abstract():
    assert not inspect.isabstract(query::GroupingSpecification)


def test_query::groupingspecification_constructor_exists():
    assert callable(query::GroupingSpecification.__init__)


def test_query::groupingspecification_constructor_args():
    sig = inspect.signature(query::GroupingSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query::queryresultspecification_is_not_abstract():
    assert not inspect.isabstract(query::QueryResultSpecification)


def test_query::queryresultspecification_constructor_exists():
    assert callable(query::QueryResultSpecification.__init__)


def test_query::queryresultspecification_constructor_args():
    sig = inspect.signature(query::QueryResultSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query::callstatement_is_not_abstract():
    assert not inspect.isabstract(query::CallStatement)


def test_query::callstatement_constructor_exists():
    assert callable(query::CallStatement.__init__)


def test_query::callstatement_constructor_args():
    sig = inspect.signature(query::CallStatement.__init__)
    params = list(sig.parameters.keys())



def test_query::updateofcolumn_is_not_abstract():
    assert not inspect.isabstract(query::UpdateOfColumn)


def test_query::updateofcolumn_constructor_exists():
    assert callable(query::UpdateOfColumn.__init__)


def test_query::updateofcolumn_constructor_args():
    sig = inspect.signature(query::UpdateOfColumn.__init__)
    params = list(sig.parameters.keys())



def test_query::columnname_is_not_abstract():
    assert not inspect.isabstract(query::ColumnName)


def test_query::columnname_constructor_exists():
    assert callable(query::ColumnName.__init__)


def test_query::columnname_constructor_args():
    sig = inspect.signature(query::ColumnName.__init__)
    params = list(sig.parameters.keys())



def test_query::procedurereference_is_not_abstract():
    assert not inspect.isabstract(query::ProcedureReference)


def test_query::procedurereference_constructor_exists():
    assert callable(query::ProcedureReference.__init__)


def test_query::procedurereference_constructor_args():
    sig = inspect.signature(query::ProcedureReference.__init__)
    params = list(sig.parameters.keys())



def test_query::supergroupelement_is_not_abstract():
    assert not inspect.isabstract(query::SuperGroupElement)


def test_query::supergroupelement_constructor_exists():
    assert callable(query::SuperGroupElement.__init__)


def test_query::supergroupelement_constructor_args():
    sig = inspect.signature(query::SuperGroupElement.__init__)
    params = list(sig.parameters.keys())



def test_query::groupingsetselement_is_not_abstract():
    assert not inspect.isabstract(query::GroupingSetsElement)


def test_query::groupingsetselement_constructor_exists():
    assert callable(query::GroupingSetsElement.__init__)


def test_query::groupingsetselement_constructor_args():
    sig = inspect.signature(query::GroupingSetsElement.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressioncasesimplecontent_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionCaseSimpleContent)


def test_query::valueexpressioncasesimplecontent_constructor_exists():
    assert callable(query::ValueExpressionCaseSimpleContent.__init__)


def test_query::valueexpressioncasesimplecontent_constructor_args():
    sig = inspect.signature(query::ValueExpressionCaseSimpleContent.__init__)
    params = list(sig.parameters.keys())



def test_query::valuesrow_is_not_abstract():
    assert not inspect.isabstract(query::ValuesRow)


def test_query::valuesrow_constructor_exists():
    assert callable(query::ValuesRow.__init__)


def test_query::valuesrow_constructor_args():
    sig = inspect.signature(query::ValuesRow.__init__)
    params = list(sig.parameters.keys())



def test_query::mergeoperationspecification_is_not_abstract():
    assert not inspect.isabstract(query::MergeOperationSpecification)


def test_query::mergeoperationspecification_constructor_exists():
    assert callable(query::MergeOperationSpecification.__init__)


def test_query::mergeoperationspecification_constructor_args():
    sig = inspect.signature(query::MergeOperationSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query::updateassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(query::UpdateAssignmentExpression)


def test_query::updateassignmentexpression_constructor_exists():
    assert callable(query::UpdateAssignmentExpression.__init__)


def test_query::updateassignmentexpression_constructor_args():
    sig = inspect.signature(query::UpdateAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_query::querysearchcondition_is_not_abstract():
    assert not inspect.isabstract(query::QuerySearchCondition)


def test_query::querysearchcondition_constructor_exists():
    assert callable(query::QuerySearchCondition.__init__)


def test_query::querysearchcondition_constructor_args():
    sig = inspect.signature(query::QuerySearchCondition.__init__)
    params = list(sig.parameters.keys())
    assert "negatedCondition" in params, "Missing parameter 'negatedCondition'"

def test_query::querysearchcondition_has_negatedCondition():
    assert hasattr(query::QuerySearchCondition, "negatedCondition")
    descriptor = None
    for klass in query::QuerySearchCondition.__mro__:
        if "negatedCondition" in klass.__dict__:
            descriptor = klass.__dict__["negatedCondition"]
            break
    assert isinstance(descriptor, property)



def test_query::withtablespecification_is_not_abstract():
    assert not inspect.isabstract(query::WithTableSpecification)


def test_query::withtablespecification_constructor_exists():
    assert callable(query::WithTableSpecification.__init__)


def test_query::withtablespecification_constructor_args():
    sig = inspect.signature(query::WithTableSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query::valueexpressioncasesearchcontent_is_not_abstract():
    assert not inspect.isabstract(query::ValueExpressionCaseSearchContent)


def test_query::valueexpressioncasesearchcontent_constructor_exists():
    assert callable(query::ValueExpressionCaseSearchContent.__init__)


def test_query::valueexpressioncasesearchcontent_constructor_args():
    sig = inspect.signature(query::ValueExpressionCaseSearchContent.__init__)
    params = list(sig.parameters.keys())



def test_query::tablereference_is_not_abstract():
    assert not inspect.isabstract(query::TableReference)


def test_query::tablereference_constructor_exists():
    assert callable(query::TableReference.__init__)


def test_query::tablereference_constructor_args():
    sig = inspect.signature(query::TableReference.__init__)
    params = list(sig.parameters.keys())



def test_query::updatesource_is_not_abstract():
    assert not inspect.isabstract(query::UpdateSource)


def test_query::updatesource_constructor_exists():
    assert callable(query::UpdateSource.__init__)


def test_query::updatesource_constructor_args():
    sig = inspect.signature(query::UpdateSource.__init__)
    params = list(sig.parameters.keys())



def test_query::cursorreference_is_not_abstract():
    assert not inspect.isabstract(query::CursorReference)


def test_query::cursorreference_constructor_exists():
    assert callable(query::CursorReference.__init__)


def test_query::cursorreference_constructor_args():
    sig = inspect.signature(query::CursorReference.__init__)
    params = list(sig.parameters.keys())



def test_query::mergesourcetable_is_not_abstract():
    assert not inspect.isabstract(query::MergeSourceTable)


def test_query::mergesourcetable_constructor_exists():
    assert callable(query::MergeSourceTable.__init__)


def test_query::mergesourcetable_constructor_args():
    sig = inspect.signature(query::MergeSourceTable.__init__)
    params = list(sig.parameters.keys())



def test_query::queryvalueexpression_is_not_abstract():
    assert not inspect.isabstract(query::QueryValueExpression)


def test_query::queryvalueexpression_constructor_exists():
    assert callable(query::QueryValueExpression.__init__)


def test_query::queryvalueexpression_constructor_args():
    sig = inspect.signature(query::QueryValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"

def test_query::queryvalueexpression_has_unaryOperator():
    assert hasattr(query::QueryValueExpression, "unaryOperator")
    descriptor = None
    for klass in query::QueryValueExpression.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_query::orderbyspecification_is_not_abstract():
    assert not inspect.isabstract(query::OrderBySpecification)


def test_query::orderbyspecification_constructor_exists():
    assert callable(query::OrderBySpecification.__init__)


def test_query::orderbyspecification_constructor_args():
    sig = inspect.signature(query::OrderBySpecification.__init__)
    params = list(sig.parameters.keys())
    assert "descending" in params, "Missing parameter 'descending'"
    assert "NullOrderingOption" in params, "Missing parameter 'NullOrderingOption'"
    assert "OrderingSpecOption" in params, "Missing parameter 'OrderingSpecOption'"

def test_query::orderbyspecification_has_descending():
    assert hasattr(query::OrderBySpecification, "descending")
    descriptor = None
    for klass in query::OrderBySpecification.__mro__:
        if "descending" in klass.__dict__:
            descriptor = klass.__dict__["descending"]
            break
    assert isinstance(descriptor, property)

def test_query::orderbyspecification_has_NullOrderingOption():
    assert hasattr(query::OrderBySpecification, "NullOrderingOption")
    descriptor = None
    for klass in query::OrderBySpecification.__mro__:
        if "NullOrderingOption" in klass.__dict__:
            descriptor = klass.__dict__["NullOrderingOption"]
            break
    assert isinstance(descriptor, property)

def test_query::orderbyspecification_has_OrderingSpecOption():
    assert hasattr(query::OrderBySpecification, "OrderingSpecOption")
    descriptor = None
    for klass in query::OrderBySpecification.__mro__:
        if "OrderingSpecOption" in klass.__dict__:
            descriptor = klass.__dict__["OrderingSpecOption"]
            break
    assert isinstance(descriptor, property)



def test_query::mergetargettable_is_not_abstract():
    assert not inspect.isabstract(query::MergeTargetTable)


def test_query::mergetargettable_constructor_exists():
    assert callable(query::MergeTargetTable.__init__)


def test_query::mergetargettable_constructor_args():
    sig = inspect.signature(query::MergeTargetTable.__init__)
    params = list(sig.parameters.keys())



def test_query::querystatement_is_not_abstract():
    assert not inspect.isabstract(query::QueryStatement)


def test_query::querystatement_constructor_exists():
    assert callable(query::QueryStatement.__init__)


def test_query::querystatement_constructor_args():
    sig = inspect.signature(query::QueryStatement.__init__)
    params = list(sig.parameters.keys())



def test_querychangestatement_is_not_abstract():
    assert not inspect.isabstract(QueryChangeStatement)


def test_querychangestatement_constructor_exists():
    assert callable(QueryChangeStatement.__init__)


def test_querychangestatement_constructor_args():
    sig = inspect.signature(QueryChangeStatement.__init__)
    params = list(sig.parameters.keys())



def test_query::querymergestatement_is_not_abstract():
    assert not inspect.isabstract(query::QueryMergeStatement)


def test_query::querymergestatement_constructor_exists():
    assert callable(query::QueryMergeStatement.__init__)


def test_query::querymergestatement_constructor_args():
    sig = inspect.signature(query::QueryMergeStatement.__init__)
    params = list(sig.parameters.keys())



def test_query::queryupdatestatement_is_not_abstract():
    assert not inspect.isabstract(query::QueryUpdateStatement)


def test_query::queryupdatestatement_constructor_exists():
    assert callable(query::QueryUpdateStatement.__init__)


def test_query::queryupdatestatement_constructor_args():
    sig = inspect.signature(query::QueryUpdateStatement.__init__)
    params = list(sig.parameters.keys())



def test_query::queryinsertstatement_is_not_abstract():
    assert not inspect.isabstract(query::QueryInsertStatement)


def test_query::queryinsertstatement_constructor_exists():
    assert callable(query::QueryInsertStatement.__init__)


def test_query::queryinsertstatement_constructor_args():
    sig = inspect.signature(query::QueryInsertStatement.__init__)
    params = list(sig.parameters.keys())



def test_query::querydeletestatement_is_not_abstract():
    assert not inspect.isabstract(query::QueryDeleteStatement)


def test_query::querydeletestatement_constructor_exists():
    assert callable(query::QueryDeleteStatement.__init__)


def test_query::querydeletestatement_constructor_args():
    sig = inspect.signature(query::QueryDeleteStatement.__init__)
    params = list(sig.parameters.keys())

def test_supergrouptype_exists():
    # Check that the Enumeration exists
    assert SuperGroupType is not None

def test_supergrouptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuperGroupType]
    expected_literals = [
        "ROLLUP",
        "GRANDTOTAL",
        "CUBE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SuperGroupType"

def test_nullorderingtype_exists():
    # Check that the Enumeration exists
    assert NullOrderingType is not None

def test_nullorderingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NullOrderingType]
    expected_literals = [
        "NONE",
        "NULLS_FIRST",
        "NULLS_LAST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NullOrderingType"

def test_valueexpressionlabeleddurationtype_exists():
    # Check that the Enumeration exists
    assert ValueExpressionLabeledDurationType is not None

def test_valueexpressionlabeleddurationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueExpressionLabeledDurationType]
    expected_literals = [
        "MONTHS",
        "YEARS",
        "MICROSECONDS",
        "DAYS",
        "MINUTES",
        "SECONDS",
        "HOURS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueExpressionLabeledDurationType"

def test_valueexpressionunaryoperator_exists():
    # Check that the Enumeration exists
    assert ValueExpressionUnaryOperator is not None

def test_valueexpressionunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueExpressionUnaryOperator]
    expected_literals = [
        "MINUS",
        "PLUS",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueExpressionUnaryOperator"

def test_orderingspectype_exists():
    # Check that the Enumeration exists
    assert OrderingSpecType is not None

def test_orderingspectype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderingSpecType]
    expected_literals = [
        "NONE",
        "DESC",
        "ASC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderingSpecType"

def test_predicatequantifiedtype_exists():
    # Check that the Enumeration exists
    assert PredicateQuantifiedType is not None

def test_predicatequantifiedtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PredicateQuantifiedType]
    expected_literals = [
        "ANY",
        "ALL",
        "SOME",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PredicateQuantifiedType"

def test_querycombinedoperator_exists():
    # Check that the Enumeration exists
    assert QueryCombinedOperator is not None

def test_querycombinedoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QueryCombinedOperator]
    expected_literals = [
        "EXCEPT",
        "UNION",
        "INTERSECT",
        "UNION_ALL",
        "EXCEPT_ALL",
        "INTERSECT_ALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QueryCombinedOperator"

def test_updatabilitytype_exists():
    # Check that the Enumeration exists
    assert UpdatabilityType is not None

def test_updatabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UpdatabilityType]
    expected_literals = [
        "READ_ONLY",
        "UPDATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UpdatabilityType"

def test_tablejoinedoperator_exists():
    # Check that the Enumeration exists
    assert TableJoinedOperator is not None

def test_tablejoinedoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TableJoinedOperator]
    expected_literals = [
        "DEFAULT_INNER",
        "EXPLICIT_INNER",
        "RIGHT_OUTER",
        "LEFT_OUTER",
        "FULL_OUTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TableJoinedOperator"

def test_valueexpressioncombinedoperator_exists():
    # Check that the Enumeration exists
    assert ValueExpressionCombinedOperator is not None

def test_valueexpressioncombinedoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueExpressionCombinedOperator]
    expected_literals = [
        "DIVIDE",
        "CONCATENATE",
        "ADD",
        "MULTIPLY",
        "SUBTRACT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueExpressionCombinedOperator"

def test_searchconditioncombinedoperator_exists():
    # Check that the Enumeration exists
    assert SearchConditionCombinedOperator is not None

def test_searchconditioncombinedoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SearchConditionCombinedOperator]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SearchConditionCombinedOperator"

def test_predicatecomparisonoperator_exists():
    # Check that the Enumeration exists
    assert PredicateComparisonOperator is not None

def test_predicatecomparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PredicateComparisonOperator]
    expected_literals = [
        "GREATER_THAN_OR_EQUAL",
        "GREATER_THAN",
        "LESS_THAN",
        "EQUAL",
        "LESS_THAN_OR_EQUAL",
        "NOT_EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PredicateComparisonOperator"


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
OrderBySpecification_strategy = st.builds(
    OrderBySpecification,
)
QuerySearchCondition_strategy = st.builds(
    QuerySearchCondition,
)
query::Predicate_strategy = st.builds(
    query::Predicate,
    negatedPredicate=
        st.booleans(),
    hasSelectivity=
        st.booleans(),
    selectivityValue=
        safe_text
)
statements::SQLControlStatement_strategy = st.builds(
    statements::SQLControlStatement,
)
Procedure_strategy = st.builds(
    Procedure,
)
MergeOperationSpecification_strategy = st.builds(
    MergeOperationSpecification,
)
UpdateSource_strategy = st.builds(
    UpdateSource,
)
query::OrderByOrdinal_strategy = st.builds(
    query::OrderByOrdinal,
    ordinalValue=
        st.integers()
)
statements::SQLDataChangeStatement_strategy = st.builds(
    statements::SQLDataChangeStatement,
)
SQLObject_strategy = st.builds(
    SQLObject,
)
query::SQLQueryObject_strategy = st.builds(
    query::SQLQueryObject,
)
Table_strategy = st.builds(
    Table,
)
ValueExpressionCase_strategy = st.builds(
    ValueExpressionCase,
)
query::ValueExpressionCaseSearch_strategy = st.builds(
    query::ValueExpressionCaseSearch,
)
Grouping_strategy = st.builds(
    Grouping,
)
query::SuperGroup_strategy = st.builds(
    query::SuperGroup,
    superGroupType=
        safe_text
)
SuperGroupElement_strategy = st.builds(
    SuperGroupElement,
)
query::SuperGroupElementExpression_strategy = st.builds(
    query::SuperGroupElementExpression,
)
query::SuperGroupElementSublist_strategy = st.builds(
    query::SuperGroupElementSublist,
)
GroupingSetsElement_strategy = st.builds(
    GroupingSetsElement,
)
query::GroupingSetsElementSublist_strategy = st.builds(
    query::GroupingSetsElementSublist,
)
query::GroupingSetsElementExpression_strategy = st.builds(
    query::GroupingSetsElementExpression,
)
GroupingSpecification_strategy = st.builds(
    GroupingSpecification,
)
query::Grouping_strategy = st.builds(
    query::Grouping,
)
query::GroupingSets_strategy = st.builds(
    query::GroupingSets,
)
QueryValueExpression_strategy = st.builds(
    QueryValueExpression,
)
query::ValueExpressionAtomic_strategy = st.builds(
    query::ValueExpressionAtomic,
)
Function_strategy = st.builds(
    Function,
)
query::MergeInsertSpecification_strategy = st.builds(
    query::MergeInsertSpecification,
)
ValueExpressionAtomic_strategy = st.builds(
    ValueExpressionAtomic,
)
query::ValueExpressionDefaultValue_strategy = st.builds(
    query::ValueExpressionDefaultValue,
)
query::ValueExpressionNullValue_strategy = st.builds(
    query::ValueExpressionNullValue,
)
query::ValueExpressionCase_strategy = st.builds(
    query::ValueExpressionCase,
)
query::ValueExpressionSimple_strategy = st.builds(
    query::ValueExpressionSimple,
    value=
        safe_text
)
PredicateQuantified_strategy = st.builds(
    PredicateQuantified,
)
PredicateIn_strategy = st.builds(
    PredicateIn,
)
Predicate_strategy = st.builds(
    Predicate,
)
query::PredicateQuantified_strategy = st.builds(
    query::PredicateQuantified,
)
query::PredicateIn_strategy = st.builds(
    query::PredicateIn,
    notIn=
        st.booleans()
)
query::OrderByResultColumn_strategy = st.builds(
    query::OrderByResultColumn,
)
QueryResultSpecification_strategy = st.builds(
    QueryResultSpecification,
)
query::ValueExpressionVariable_strategy = st.builds(
    query::ValueExpressionVariable,
)
query::ResultTableAllColumns_strategy = st.builds(
    query::ResultTableAllColumns,
)
TableReference_strategy = st.builds(
    TableReference,
)
query::TableExpression_strategy = st.builds(
    query::TableExpression,
)
query::TableNested_strategy = st.builds(
    query::TableNested,
)
QueryExpressionBody_strategy = st.builds(
    QueryExpressionBody,
)
query::QueryValues_strategy = st.builds(
    query::QueryValues,
)
query::ValueExpressionScalarSelect_strategy = st.builds(
    query::ValueExpressionScalarSelect,
)
query::ValueExpressionRow_strategy = st.builds(
    query::ValueExpressionRow,
)
query::UpdateSourceExprList_strategy = st.builds(
    query::UpdateSourceExprList,
)
expressions::QueryExpression_strategy = st.builds(
    expressions::QueryExpression,
)
query::ValueExpressionCaseSimple_strategy = st.builds(
    query::ValueExpressionCaseSimple,
)
query::ValueExpressionNested_strategy = st.builds(
    query::ValueExpressionNested,
)
query::ValueExpressionLabeledDuration_strategy = st.builds(
    query::ValueExpressionLabeledDuration,
    labeledDurationType=
        safe_text
)
query::ValueExpressionCombined_strategy = st.builds(
    query::ValueExpressionCombined,
    combinedOperator=
        safe_text
)
query::ValueExpressionFunction_strategy = st.builds(
    query::ValueExpressionFunction,
    distinct=
        st.booleans(),
    columnFunction=
        st.booleans(),
    specialRegister=
        st.booleans()
)
query::ValueExpressionCast_strategy = st.builds(
    query::ValueExpressionCast,
)
query::GroupingExpression_strategy = st.builds(
    query::GroupingExpression,
)
query::PredicateQuantifiedValueSelect_strategy = st.builds(
    query::PredicateQuantifiedValueSelect,
    quantifiedType=
        safe_text,
    comparisonOperator=
        safe_text
)
query::PredicateQuantifiedRowSelect_strategy = st.builds(
    query::PredicateQuantifiedRowSelect,
    quantifiedType=
        safe_text
)
query::PredicateInValueSelect_strategy = st.builds(
    query::PredicateInValueSelect,
)
query::PredicateInValueRowSelect_strategy = st.builds(
    query::PredicateInValueRowSelect,
)
query::PredicateInValueList_strategy = st.builds(
    query::PredicateInValueList,
)
query::PredicateBetween_strategy = st.builds(
    query::PredicateBetween,
    notBetween=
        st.booleans()
)
query::PredicateLike_strategy = st.builds(
    query::PredicateLike,
    notLike=
        st.booleans()
)
query::PredicateBasic_strategy = st.builds(
    query::PredicateBasic,
    comparisonOperator=
        safe_text
)
query::ResultColumn_strategy = st.builds(
    query::ResultColumn,
)
query::OrderByValueExpression_strategy = st.builds(
    query::OrderByValueExpression,
)
query::PredicateIsNull_strategy = st.builds(
    query::PredicateIsNull,
    notNull=
        st.booleans()
)
query::QueryNested_strategy = st.builds(
    query::QueryNested,
)
query::UpdateSourceQuery_strategy = st.builds(
    query::UpdateSourceQuery,
)
query::PredicateExists_strategy = st.builds(
    query::PredicateExists,
)
DataType_strategy = st.builds(
    DataType,
)
expressions::ValueExpression_strategy = st.builds(
    expressions::ValueExpression,
)
TableExpression_strategy = st.builds(
    TableExpression,
)
query::TableFunction_strategy = st.builds(
    query::TableFunction,
)
query::TableQueryLateral_strategy = st.builds(
    query::TableQueryLateral,
)
query::WithTableReference_strategy = st.builds(
    query::WithTableReference,
)
query::QueryExpressionBody_strategy = st.builds(
    query::QueryExpressionBody,
    rowFetchLimit=
        st.integers()
)
query::SearchConditionNested_strategy = st.builds(
    query::SearchConditionNested,
)
query::QuerySelect_strategy = st.builds(
    query::QuerySelect,
    distinct=
        st.booleans()
)
query::QueryCombined_strategy = st.builds(
    query::QueryCombined,
    combinedOperator=
        safe_text
)
query::SearchConditionCombined_strategy = st.builds(
    query::SearchConditionCombined,
    combinedOperator=
        safe_text
)
query::TableJoined_strategy = st.builds(
    query::TableJoined,
    joinOperator=
        safe_text
)
expressions::SearchCondition_strategy = st.builds(
    expressions::SearchCondition,
)
query::MergeUpdateSpecification_strategy = st.builds(
    query::MergeUpdateSpecification,
)
QueryStatement_strategy = st.builds(
    QueryStatement,
)
query::QueryChangeStatement_strategy = st.builds(
    query::QueryChangeStatement,
)
query::QuerySelectStatement_strategy = st.builds(
    query::QuerySelectStatement,
)
query::ValueExpressionColumn_strategy = st.builds(
    query::ValueExpressionColumn,
)
query::TableInDatabase_strategy = st.builds(
    query::TableInDatabase,
)
statements::SQLDataStatement_strategy = st.builds(
    statements::SQLDataStatement,
)
SQLQueryObject_strategy = st.builds(
    SQLQueryObject,
)
query::TableCorrelation_strategy = st.builds(
    query::TableCorrelation,
)
query::QueryExpressionRoot_strategy = st.builds(
    query::QueryExpressionRoot,
)
query::UpdatabilityExpression_strategy = st.builds(
    query::UpdatabilityExpression,
    updatabilityType=
        safe_text
)
query::MergeOnCondition_strategy = st.builds(
    query::MergeOnCondition,
)
query::ValueExpressionCaseElse_strategy = st.builds(
    query::ValueExpressionCaseElse,
)
query::GroupingSpecification_strategy = st.builds(
    query::GroupingSpecification,
)
query::QueryResultSpecification_strategy = st.builds(
    query::QueryResultSpecification,
)
query::CallStatement_strategy = st.builds(
    query::CallStatement,
)
query::UpdateOfColumn_strategy = st.builds(
    query::UpdateOfColumn,
)
query::ColumnName_strategy = st.builds(
    query::ColumnName,
)
query::ProcedureReference_strategy = st.builds(
    query::ProcedureReference,
)
query::SuperGroupElement_strategy = st.builds(
    query::SuperGroupElement,
)
query::GroupingSetsElement_strategy = st.builds(
    query::GroupingSetsElement,
)
query::ValueExpressionCaseSimpleContent_strategy = st.builds(
    query::ValueExpressionCaseSimpleContent,
)
query::ValuesRow_strategy = st.builds(
    query::ValuesRow,
)
query::MergeOperationSpecification_strategy = st.builds(
    query::MergeOperationSpecification,
)
query::UpdateAssignmentExpression_strategy = st.builds(
    query::UpdateAssignmentExpression,
)
query::QuerySearchCondition_strategy = st.builds(
    query::QuerySearchCondition,
    negatedCondition=
        st.booleans()
)
query::WithTableSpecification_strategy = st.builds(
    query::WithTableSpecification,
)
query::ValueExpressionCaseSearchContent_strategy = st.builds(
    query::ValueExpressionCaseSearchContent,
)
query::TableReference_strategy = st.builds(
    query::TableReference,
)
query::UpdateSource_strategy = st.builds(
    query::UpdateSource,
)
query::CursorReference_strategy = st.builds(
    query::CursorReference,
)
query::MergeSourceTable_strategy = st.builds(
    query::MergeSourceTable,
)
query::QueryValueExpression_strategy = st.builds(
    query::QueryValueExpression,
    unaryOperator=
        safe_text
)
query::OrderBySpecification_strategy = st.builds(
    query::OrderBySpecification,
    descending=
        st.booleans(),
    NullOrderingOption=
        safe_text,
    OrderingSpecOption=
        safe_text
)
query::MergeTargetTable_strategy = st.builds(
    query::MergeTargetTable,
)
query::QueryStatement_strategy = st.builds(
    query::QueryStatement,
)
QueryChangeStatement_strategy = st.builds(
    QueryChangeStatement,
)
query::QueryMergeStatement_strategy = st.builds(
    query::QueryMergeStatement,
)
query::QueryUpdateStatement_strategy = st.builds(
    query::QueryUpdateStatement,
)
query::QueryInsertStatement_strategy = st.builds(
    query::QueryInsertStatement,
)
query::QueryDeleteStatement_strategy = st.builds(
    query::QueryDeleteStatement,
)

@given(instance=OrderBySpecification_strategy)
@settings(max_examples=50)
def test_orderbyspecification_instantiation(instance):
    assert isinstance(instance, OrderBySpecification)

@given(instance=QuerySearchCondition_strategy)
@settings(max_examples=50)
def test_querysearchcondition_instantiation(instance):
    assert isinstance(instance, QuerySearchCondition)

@given(instance=query::Predicate_strategy)
@settings(max_examples=50)
def test_query::predicate_instantiation(instance):
    assert isinstance(instance, query::Predicate)

@given(instance=query::Predicate_strategy)
def test_query::predicate_negatedPredicate_type(instance):
    assert isinstance(instance.negatedPredicate, bool)


@given(instance=query::Predicate_strategy)
def test_query::predicate_negatedPredicate_setter(instance):
    original = instance.negatedPredicate
    instance.negatedPredicate = original
    assert instance.negatedPredicate == original

@given(instance=query::Predicate_strategy)
def test_query::predicate_hasSelectivity_type(instance):
    assert isinstance(instance.hasSelectivity, bool)


@given(instance=query::Predicate_strategy)
def test_query::predicate_hasSelectivity_setter(instance):
    original = instance.hasSelectivity
    instance.hasSelectivity = original
    assert instance.hasSelectivity == original

@given(instance=query::Predicate_strategy)
def test_query::predicate_selectivityValue_type(instance):
    assert isinstance(instance.selectivityValue, str)


@given(instance=query::Predicate_strategy)
def test_query::predicate_selectivityValue_setter(instance):
    original = instance.selectivityValue
    instance.selectivityValue = original
    assert instance.selectivityValue == original

@given(instance=statements::SQLControlStatement_strategy)
@settings(max_examples=50)
def test_statements::sqlcontrolstatement_instantiation(instance):
    assert isinstance(instance, statements::SQLControlStatement)

@given(instance=Procedure_strategy)
@settings(max_examples=50)
def test_procedure_instantiation(instance):
    assert isinstance(instance, Procedure)

@given(instance=MergeOperationSpecification_strategy)
@settings(max_examples=50)
def test_mergeoperationspecification_instantiation(instance):
    assert isinstance(instance, MergeOperationSpecification)

@given(instance=UpdateSource_strategy)
@settings(max_examples=50)
def test_updatesource_instantiation(instance):
    assert isinstance(instance, UpdateSource)

@given(instance=query::OrderByOrdinal_strategy)
@settings(max_examples=50)
def test_query::orderbyordinal_instantiation(instance):
    assert isinstance(instance, query::OrderByOrdinal)

@given(instance=query::OrderByOrdinal_strategy)
def test_query::orderbyordinal_ordinalValue_type(instance):
    assert isinstance(instance.ordinalValue, int)


@given(instance=query::OrderByOrdinal_strategy)
def test_query::orderbyordinal_ordinalValue_setter(instance):
    original = instance.ordinalValue
    instance.ordinalValue = original
    assert instance.ordinalValue == original

@given(instance=statements::SQLDataChangeStatement_strategy)
@settings(max_examples=50)
def test_statements::sqldatachangestatement_instantiation(instance):
    assert isinstance(instance, statements::SQLDataChangeStatement)

@given(instance=SQLObject_strategy)
@settings(max_examples=50)
def test_sqlobject_instantiation(instance):
    assert isinstance(instance, SQLObject)

@given(instance=query::SQLQueryObject_strategy)
@settings(max_examples=50)
def test_query::sqlqueryobject_instantiation(instance):
    assert isinstance(instance, query::SQLQueryObject)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=query::SQLQueryObject_strategy)
@settings(max_examples=30)
def test_query::sqlqueryobject_setsql_changes_state(instance):
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
        assert has_statements, f"Function 'setSQL' in query::SQLQueryObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSQL' in query::SQLQueryObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSQL' in query::SQLQueryObject is not implemented or raised an error")

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=ValueExpressionCase_strategy)
@settings(max_examples=50)
def test_valueexpressioncase_instantiation(instance):
    assert isinstance(instance, ValueExpressionCase)

@given(instance=query::ValueExpressionCaseSearch_strategy)
@settings(max_examples=50)
def test_query::valueexpressioncasesearch_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionCaseSearch)

@given(instance=Grouping_strategy)
@settings(max_examples=50)
def test_grouping_instantiation(instance):
    assert isinstance(instance, Grouping)

@given(instance=query::SuperGroup_strategy)
@settings(max_examples=50)
def test_query::supergroup_instantiation(instance):
    assert isinstance(instance, query::SuperGroup)

@given(instance=query::SuperGroup_strategy)
def test_query::supergroup_superGroupType_type(instance):
    assert isinstance(instance.superGroupType, str)


@given(instance=query::SuperGroup_strategy)
def test_query::supergroup_superGroupType_setter(instance):
    original = instance.superGroupType
    instance.superGroupType = original
    assert instance.superGroupType == original

@given(instance=SuperGroupElement_strategy)
@settings(max_examples=50)
def test_supergroupelement_instantiation(instance):
    assert isinstance(instance, SuperGroupElement)

@given(instance=query::SuperGroupElementExpression_strategy)
@settings(max_examples=50)
def test_query::supergroupelementexpression_instantiation(instance):
    assert isinstance(instance, query::SuperGroupElementExpression)

@given(instance=query::SuperGroupElementSublist_strategy)
@settings(max_examples=50)
def test_query::supergroupelementsublist_instantiation(instance):
    assert isinstance(instance, query::SuperGroupElementSublist)

@given(instance=GroupingSetsElement_strategy)
@settings(max_examples=50)
def test_groupingsetselement_instantiation(instance):
    assert isinstance(instance, GroupingSetsElement)

@given(instance=query::GroupingSetsElementSublist_strategy)
@settings(max_examples=50)
def test_query::groupingsetselementsublist_instantiation(instance):
    assert isinstance(instance, query::GroupingSetsElementSublist)

@given(instance=query::GroupingSetsElementExpression_strategy)
@settings(max_examples=50)
def test_query::groupingsetselementexpression_instantiation(instance):
    assert isinstance(instance, query::GroupingSetsElementExpression)

@given(instance=GroupingSpecification_strategy)
@settings(max_examples=50)
def test_groupingspecification_instantiation(instance):
    assert isinstance(instance, GroupingSpecification)

@given(instance=query::Grouping_strategy)
@settings(max_examples=50)
def test_query::grouping_instantiation(instance):
    assert isinstance(instance, query::Grouping)

@given(instance=query::GroupingSets_strategy)
@settings(max_examples=50)
def test_query::groupingsets_instantiation(instance):
    assert isinstance(instance, query::GroupingSets)

@given(instance=QueryValueExpression_strategy)
@settings(max_examples=50)
def test_queryvalueexpression_instantiation(instance):
    assert isinstance(instance, QueryValueExpression)

@given(instance=query::ValueExpressionAtomic_strategy)
@settings(max_examples=50)
def test_query::valueexpressionatomic_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionAtomic)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=query::MergeInsertSpecification_strategy)
@settings(max_examples=50)
def test_query::mergeinsertspecification_instantiation(instance):
    assert isinstance(instance, query::MergeInsertSpecification)

@given(instance=ValueExpressionAtomic_strategy)
@settings(max_examples=50)
def test_valueexpressionatomic_instantiation(instance):
    assert isinstance(instance, ValueExpressionAtomic)

@given(instance=query::ValueExpressionDefaultValue_strategy)
@settings(max_examples=50)
def test_query::valueexpressiondefaultvalue_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionDefaultValue)

@given(instance=query::ValueExpressionNullValue_strategy)
@settings(max_examples=50)
def test_query::valueexpressionnullvalue_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionNullValue)

@given(instance=query::ValueExpressionCase_strategy)
@settings(max_examples=50)
def test_query::valueexpressioncase_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionCase)

@given(instance=query::ValueExpressionSimple_strategy)
@settings(max_examples=50)
def test_query::valueexpressionsimple_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionSimple)

@given(instance=query::ValueExpressionSimple_strategy)
def test_query::valueexpressionsimple_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=query::ValueExpressionSimple_strategy)
def test_query::valueexpressionsimple_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PredicateQuantified_strategy)
@settings(max_examples=50)
def test_predicatequantified_instantiation(instance):
    assert isinstance(instance, PredicateQuantified)

@given(instance=PredicateIn_strategy)
@settings(max_examples=50)
def test_predicatein_instantiation(instance):
    assert isinstance(instance, PredicateIn)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=query::PredicateQuantified_strategy)
@settings(max_examples=50)
def test_query::predicatequantified_instantiation(instance):
    assert isinstance(instance, query::PredicateQuantified)

@given(instance=query::PredicateIn_strategy)
@settings(max_examples=50)
def test_query::predicatein_instantiation(instance):
    assert isinstance(instance, query::PredicateIn)

@given(instance=query::PredicateIn_strategy)
def test_query::predicatein_notIn_type(instance):
    assert isinstance(instance.notIn, bool)


@given(instance=query::PredicateIn_strategy)
def test_query::predicatein_notIn_setter(instance):
    original = instance.notIn
    instance.notIn = original
    assert instance.notIn == original

@given(instance=query::OrderByResultColumn_strategy)
@settings(max_examples=50)
def test_query::orderbyresultcolumn_instantiation(instance):
    assert isinstance(instance, query::OrderByResultColumn)

@given(instance=QueryResultSpecification_strategy)
@settings(max_examples=50)
def test_queryresultspecification_instantiation(instance):
    assert isinstance(instance, QueryResultSpecification)

@given(instance=query::ValueExpressionVariable_strategy)
@settings(max_examples=50)
def test_query::valueexpressionvariable_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionVariable)

@given(instance=query::ResultTableAllColumns_strategy)
@settings(max_examples=50)
def test_query::resulttableallcolumns_instantiation(instance):
    assert isinstance(instance, query::ResultTableAllColumns)

@given(instance=TableReference_strategy)
@settings(max_examples=50)
def test_tablereference_instantiation(instance):
    assert isinstance(instance, TableReference)

@given(instance=query::TableExpression_strategy)
@settings(max_examples=50)
def test_query::tableexpression_instantiation(instance):
    assert isinstance(instance, query::TableExpression)

@given(instance=query::TableNested_strategy)
@settings(max_examples=50)
def test_query::tablenested_instantiation(instance):
    assert isinstance(instance, query::TableNested)

@given(instance=QueryExpressionBody_strategy)
@settings(max_examples=50)
def test_queryexpressionbody_instantiation(instance):
    assert isinstance(instance, QueryExpressionBody)

@given(instance=query::QueryValues_strategy)
@settings(max_examples=50)
def test_query::queryvalues_instantiation(instance):
    assert isinstance(instance, query::QueryValues)

@given(instance=query::ValueExpressionScalarSelect_strategy)
@settings(max_examples=50)
def test_query::valueexpressionscalarselect_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionScalarSelect)

@given(instance=query::ValueExpressionRow_strategy)
@settings(max_examples=50)
def test_query::valueexpressionrow_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionRow)

@given(instance=query::UpdateSourceExprList_strategy)
@settings(max_examples=50)
def test_query::updatesourceexprlist_instantiation(instance):
    assert isinstance(instance, query::UpdateSourceExprList)

@given(instance=expressions::QueryExpression_strategy)
@settings(max_examples=50)
def test_expressions::queryexpression_instantiation(instance):
    assert isinstance(instance, expressions::QueryExpression)

@given(instance=query::ValueExpressionCaseSimple_strategy)
@settings(max_examples=50)
def test_query::valueexpressioncasesimple_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionCaseSimple)

@given(instance=query::ValueExpressionNested_strategy)
@settings(max_examples=50)
def test_query::valueexpressionnested_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionNested)

@given(instance=query::ValueExpressionLabeledDuration_strategy)
@settings(max_examples=50)
def test_query::valueexpressionlabeledduration_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionLabeledDuration)

@given(instance=query::ValueExpressionLabeledDuration_strategy)
def test_query::valueexpressionlabeledduration_labeledDurationType_type(instance):
    assert isinstance(instance.labeledDurationType, str)


@given(instance=query::ValueExpressionLabeledDuration_strategy)
def test_query::valueexpressionlabeledduration_labeledDurationType_setter(instance):
    original = instance.labeledDurationType
    instance.labeledDurationType = original
    assert instance.labeledDurationType == original

@given(instance=query::ValueExpressionCombined_strategy)
@settings(max_examples=50)
def test_query::valueexpressioncombined_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionCombined)

@given(instance=query::ValueExpressionCombined_strategy)
def test_query::valueexpressioncombined_combinedOperator_type(instance):
    assert isinstance(instance.combinedOperator, str)


@given(instance=query::ValueExpressionCombined_strategy)
def test_query::valueexpressioncombined_combinedOperator_setter(instance):
    original = instance.combinedOperator
    instance.combinedOperator = original
    assert instance.combinedOperator == original

@given(instance=query::ValueExpressionFunction_strategy)
@settings(max_examples=50)
def test_query::valueexpressionfunction_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionFunction)

@given(instance=query::ValueExpressionFunction_strategy)
def test_query::valueexpressionfunction_distinct_type(instance):
    assert isinstance(instance.distinct, bool)


@given(instance=query::ValueExpressionFunction_strategy)
def test_query::valueexpressionfunction_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=query::ValueExpressionFunction_strategy)
def test_query::valueexpressionfunction_columnFunction_type(instance):
    assert isinstance(instance.columnFunction, bool)


@given(instance=query::ValueExpressionFunction_strategy)
def test_query::valueexpressionfunction_columnFunction_setter(instance):
    original = instance.columnFunction
    instance.columnFunction = original
    assert instance.columnFunction == original

@given(instance=query::ValueExpressionFunction_strategy)
def test_query::valueexpressionfunction_specialRegister_type(instance):
    assert isinstance(instance.specialRegister, bool)


@given(instance=query::ValueExpressionFunction_strategy)
def test_query::valueexpressionfunction_specialRegister_setter(instance):
    original = instance.specialRegister
    instance.specialRegister = original
    assert instance.specialRegister == original

@given(instance=query::ValueExpressionCast_strategy)
@settings(max_examples=50)
def test_query::valueexpressioncast_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionCast)

@given(instance=query::GroupingExpression_strategy)
@settings(max_examples=50)
def test_query::groupingexpression_instantiation(instance):
    assert isinstance(instance, query::GroupingExpression)

@given(instance=query::PredicateQuantifiedValueSelect_strategy)
@settings(max_examples=50)
def test_query::predicatequantifiedvalueselect_instantiation(instance):
    assert isinstance(instance, query::PredicateQuantifiedValueSelect)

@given(instance=query::PredicateQuantifiedValueSelect_strategy)
def test_query::predicatequantifiedvalueselect_quantifiedType_type(instance):
    assert isinstance(instance.quantifiedType, str)


@given(instance=query::PredicateQuantifiedValueSelect_strategy)
def test_query::predicatequantifiedvalueselect_quantifiedType_setter(instance):
    original = instance.quantifiedType
    instance.quantifiedType = original
    assert instance.quantifiedType == original

@given(instance=query::PredicateQuantifiedValueSelect_strategy)
def test_query::predicatequantifiedvalueselect_comparisonOperator_type(instance):
    assert isinstance(instance.comparisonOperator, str)


@given(instance=query::PredicateQuantifiedValueSelect_strategy)
def test_query::predicatequantifiedvalueselect_comparisonOperator_setter(instance):
    original = instance.comparisonOperator
    instance.comparisonOperator = original
    assert instance.comparisonOperator == original

@given(instance=query::PredicateQuantifiedRowSelect_strategy)
@settings(max_examples=50)
def test_query::predicatequantifiedrowselect_instantiation(instance):
    assert isinstance(instance, query::PredicateQuantifiedRowSelect)

@given(instance=query::PredicateQuantifiedRowSelect_strategy)
def test_query::predicatequantifiedrowselect_quantifiedType_type(instance):
    assert isinstance(instance.quantifiedType, str)


@given(instance=query::PredicateQuantifiedRowSelect_strategy)
def test_query::predicatequantifiedrowselect_quantifiedType_setter(instance):
    original = instance.quantifiedType
    instance.quantifiedType = original
    assert instance.quantifiedType == original

@given(instance=query::PredicateInValueSelect_strategy)
@settings(max_examples=50)
def test_query::predicateinvalueselect_instantiation(instance):
    assert isinstance(instance, query::PredicateInValueSelect)

@given(instance=query::PredicateInValueRowSelect_strategy)
@settings(max_examples=50)
def test_query::predicateinvaluerowselect_instantiation(instance):
    assert isinstance(instance, query::PredicateInValueRowSelect)

@given(instance=query::PredicateInValueList_strategy)
@settings(max_examples=50)
def test_query::predicateinvaluelist_instantiation(instance):
    assert isinstance(instance, query::PredicateInValueList)

@given(instance=query::PredicateBetween_strategy)
@settings(max_examples=50)
def test_query::predicatebetween_instantiation(instance):
    assert isinstance(instance, query::PredicateBetween)

@given(instance=query::PredicateBetween_strategy)
def test_query::predicatebetween_notBetween_type(instance):
    assert isinstance(instance.notBetween, bool)


@given(instance=query::PredicateBetween_strategy)
def test_query::predicatebetween_notBetween_setter(instance):
    original = instance.notBetween
    instance.notBetween = original
    assert instance.notBetween == original

@given(instance=query::PredicateLike_strategy)
@settings(max_examples=50)
def test_query::predicatelike_instantiation(instance):
    assert isinstance(instance, query::PredicateLike)

@given(instance=query::PredicateLike_strategy)
def test_query::predicatelike_notLike_type(instance):
    assert isinstance(instance.notLike, bool)


@given(instance=query::PredicateLike_strategy)
def test_query::predicatelike_notLike_setter(instance):
    original = instance.notLike
    instance.notLike = original
    assert instance.notLike == original

@given(instance=query::PredicateBasic_strategy)
@settings(max_examples=50)
def test_query::predicatebasic_instantiation(instance):
    assert isinstance(instance, query::PredicateBasic)

@given(instance=query::PredicateBasic_strategy)
def test_query::predicatebasic_comparisonOperator_type(instance):
    assert isinstance(instance.comparisonOperator, str)


@given(instance=query::PredicateBasic_strategy)
def test_query::predicatebasic_comparisonOperator_setter(instance):
    original = instance.comparisonOperator
    instance.comparisonOperator = original
    assert instance.comparisonOperator == original

@given(instance=query::ResultColumn_strategy)
@settings(max_examples=50)
def test_query::resultcolumn_instantiation(instance):
    assert isinstance(instance, query::ResultColumn)

@given(instance=query::OrderByValueExpression_strategy)
@settings(max_examples=50)
def test_query::orderbyvalueexpression_instantiation(instance):
    assert isinstance(instance, query::OrderByValueExpression)

@given(instance=query::PredicateIsNull_strategy)
@settings(max_examples=50)
def test_query::predicateisnull_instantiation(instance):
    assert isinstance(instance, query::PredicateIsNull)

@given(instance=query::PredicateIsNull_strategy)
def test_query::predicateisnull_notNull_type(instance):
    assert isinstance(instance.notNull, bool)


@given(instance=query::PredicateIsNull_strategy)
def test_query::predicateisnull_notNull_setter(instance):
    original = instance.notNull
    instance.notNull = original
    assert instance.notNull == original

@given(instance=query::QueryNested_strategy)
@settings(max_examples=50)
def test_query::querynested_instantiation(instance):
    assert isinstance(instance, query::QueryNested)

@given(instance=query::UpdateSourceQuery_strategy)
@settings(max_examples=50)
def test_query::updatesourcequery_instantiation(instance):
    assert isinstance(instance, query::UpdateSourceQuery)

@given(instance=query::PredicateExists_strategy)
@settings(max_examples=50)
def test_query::predicateexists_instantiation(instance):
    assert isinstance(instance, query::PredicateExists)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=expressions::ValueExpression_strategy)
@settings(max_examples=50)
def test_expressions::valueexpression_instantiation(instance):
    assert isinstance(instance, expressions::ValueExpression)

@given(instance=TableExpression_strategy)
@settings(max_examples=50)
def test_tableexpression_instantiation(instance):
    assert isinstance(instance, TableExpression)

@given(instance=query::TableFunction_strategy)
@settings(max_examples=50)
def test_query::tablefunction_instantiation(instance):
    assert isinstance(instance, query::TableFunction)

@given(instance=query::TableQueryLateral_strategy)
@settings(max_examples=50)
def test_query::tablequerylateral_instantiation(instance):
    assert isinstance(instance, query::TableQueryLateral)

@given(instance=query::WithTableReference_strategy)
@settings(max_examples=50)
def test_query::withtablereference_instantiation(instance):
    assert isinstance(instance, query::WithTableReference)

@given(instance=query::QueryExpressionBody_strategy)
@settings(max_examples=50)
def test_query::queryexpressionbody_instantiation(instance):
    assert isinstance(instance, query::QueryExpressionBody)

@given(instance=query::QueryExpressionBody_strategy)
def test_query::queryexpressionbody_rowFetchLimit_type(instance):
    assert isinstance(instance.rowFetchLimit, int)


@given(instance=query::QueryExpressionBody_strategy)
def test_query::queryexpressionbody_rowFetchLimit_setter(instance):
    original = instance.rowFetchLimit
    instance.rowFetchLimit = original
    assert instance.rowFetchLimit == original

@given(instance=query::SearchConditionNested_strategy)
@settings(max_examples=50)
def test_query::searchconditionnested_instantiation(instance):
    assert isinstance(instance, query::SearchConditionNested)

@given(instance=query::QuerySelect_strategy)
@settings(max_examples=50)
def test_query::queryselect_instantiation(instance):
    assert isinstance(instance, query::QuerySelect)

@given(instance=query::QuerySelect_strategy)
def test_query::queryselect_distinct_type(instance):
    assert isinstance(instance.distinct, bool)


@given(instance=query::QuerySelect_strategy)
def test_query::queryselect_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=query::QueryCombined_strategy)
@settings(max_examples=50)
def test_query::querycombined_instantiation(instance):
    assert isinstance(instance, query::QueryCombined)

@given(instance=query::QueryCombined_strategy)
def test_query::querycombined_combinedOperator_type(instance):
    assert isinstance(instance.combinedOperator, str)


@given(instance=query::QueryCombined_strategy)
def test_query::querycombined_combinedOperator_setter(instance):
    original = instance.combinedOperator
    instance.combinedOperator = original
    assert instance.combinedOperator == original

@given(instance=query::SearchConditionCombined_strategy)
@settings(max_examples=50)
def test_query::searchconditioncombined_instantiation(instance):
    assert isinstance(instance, query::SearchConditionCombined)

@given(instance=query::SearchConditionCombined_strategy)
def test_query::searchconditioncombined_combinedOperator_type(instance):
    assert isinstance(instance.combinedOperator, str)


@given(instance=query::SearchConditionCombined_strategy)
def test_query::searchconditioncombined_combinedOperator_setter(instance):
    original = instance.combinedOperator
    instance.combinedOperator = original
    assert instance.combinedOperator == original

@given(instance=query::TableJoined_strategy)
@settings(max_examples=50)
def test_query::tablejoined_instantiation(instance):
    assert isinstance(instance, query::TableJoined)

@given(instance=query::TableJoined_strategy)
def test_query::tablejoined_joinOperator_type(instance):
    assert isinstance(instance.joinOperator, str)


@given(instance=query::TableJoined_strategy)
def test_query::tablejoined_joinOperator_setter(instance):
    original = instance.joinOperator
    instance.joinOperator = original
    assert instance.joinOperator == original

@given(instance=expressions::SearchCondition_strategy)
@settings(max_examples=50)
def test_expressions::searchcondition_instantiation(instance):
    assert isinstance(instance, expressions::SearchCondition)

@given(instance=query::MergeUpdateSpecification_strategy)
@settings(max_examples=50)
def test_query::mergeupdatespecification_instantiation(instance):
    assert isinstance(instance, query::MergeUpdateSpecification)

@given(instance=QueryStatement_strategy)
@settings(max_examples=50)
def test_querystatement_instantiation(instance):
    assert isinstance(instance, QueryStatement)

@given(instance=query::QueryChangeStatement_strategy)
@settings(max_examples=50)
def test_query::querychangestatement_instantiation(instance):
    assert isinstance(instance, query::QueryChangeStatement)

@given(instance=query::QuerySelectStatement_strategy)
@settings(max_examples=50)
def test_query::queryselectstatement_instantiation(instance):
    assert isinstance(instance, query::QuerySelectStatement)

@given(instance=query::ValueExpressionColumn_strategy)
@settings(max_examples=50)
def test_query::valueexpressioncolumn_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionColumn)

@given(instance=query::TableInDatabase_strategy)
@settings(max_examples=50)
def test_query::tableindatabase_instantiation(instance):
    assert isinstance(instance, query::TableInDatabase)

@given(instance=statements::SQLDataStatement_strategy)
@settings(max_examples=50)
def test_statements::sqldatastatement_instantiation(instance):
    assert isinstance(instance, statements::SQLDataStatement)

@given(instance=SQLQueryObject_strategy)
@settings(max_examples=50)
def test_sqlqueryobject_instantiation(instance):
    assert isinstance(instance, SQLQueryObject)

@given(instance=query::TableCorrelation_strategy)
@settings(max_examples=50)
def test_query::tablecorrelation_instantiation(instance):
    assert isinstance(instance, query::TableCorrelation)

@given(instance=query::QueryExpressionRoot_strategy)
@settings(max_examples=50)
def test_query::queryexpressionroot_instantiation(instance):
    assert isinstance(instance, query::QueryExpressionRoot)

@given(instance=query::UpdatabilityExpression_strategy)
@settings(max_examples=50)
def test_query::updatabilityexpression_instantiation(instance):
    assert isinstance(instance, query::UpdatabilityExpression)

@given(instance=query::UpdatabilityExpression_strategy)
def test_query::updatabilityexpression_updatabilityType_type(instance):
    assert isinstance(instance.updatabilityType, str)


@given(instance=query::UpdatabilityExpression_strategy)
def test_query::updatabilityexpression_updatabilityType_setter(instance):
    original = instance.updatabilityType
    instance.updatabilityType = original
    assert instance.updatabilityType == original

@given(instance=query::MergeOnCondition_strategy)
@settings(max_examples=50)
def test_query::mergeoncondition_instantiation(instance):
    assert isinstance(instance, query::MergeOnCondition)

@given(instance=query::ValueExpressionCaseElse_strategy)
@settings(max_examples=50)
def test_query::valueexpressioncaseelse_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionCaseElse)

@given(instance=query::GroupingSpecification_strategy)
@settings(max_examples=50)
def test_query::groupingspecification_instantiation(instance):
    assert isinstance(instance, query::GroupingSpecification)

@given(instance=query::QueryResultSpecification_strategy)
@settings(max_examples=50)
def test_query::queryresultspecification_instantiation(instance):
    assert isinstance(instance, query::QueryResultSpecification)

@given(instance=query::CallStatement_strategy)
@settings(max_examples=50)
def test_query::callstatement_instantiation(instance):
    assert isinstance(instance, query::CallStatement)

@given(instance=query::UpdateOfColumn_strategy)
@settings(max_examples=50)
def test_query::updateofcolumn_instantiation(instance):
    assert isinstance(instance, query::UpdateOfColumn)

@given(instance=query::ColumnName_strategy)
@settings(max_examples=50)
def test_query::columnname_instantiation(instance):
    assert isinstance(instance, query::ColumnName)

@given(instance=query::ProcedureReference_strategy)
@settings(max_examples=50)
def test_query::procedurereference_instantiation(instance):
    assert isinstance(instance, query::ProcedureReference)

@given(instance=query::SuperGroupElement_strategy)
@settings(max_examples=50)
def test_query::supergroupelement_instantiation(instance):
    assert isinstance(instance, query::SuperGroupElement)

@given(instance=query::GroupingSetsElement_strategy)
@settings(max_examples=50)
def test_query::groupingsetselement_instantiation(instance):
    assert isinstance(instance, query::GroupingSetsElement)

@given(instance=query::ValueExpressionCaseSimpleContent_strategy)
@settings(max_examples=50)
def test_query::valueexpressioncasesimplecontent_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionCaseSimpleContent)

@given(instance=query::ValuesRow_strategy)
@settings(max_examples=50)
def test_query::valuesrow_instantiation(instance):
    assert isinstance(instance, query::ValuesRow)

@given(instance=query::MergeOperationSpecification_strategy)
@settings(max_examples=50)
def test_query::mergeoperationspecification_instantiation(instance):
    assert isinstance(instance, query::MergeOperationSpecification)

@given(instance=query::UpdateAssignmentExpression_strategy)
@settings(max_examples=50)
def test_query::updateassignmentexpression_instantiation(instance):
    assert isinstance(instance, query::UpdateAssignmentExpression)

@given(instance=query::QuerySearchCondition_strategy)
@settings(max_examples=50)
def test_query::querysearchcondition_instantiation(instance):
    assert isinstance(instance, query::QuerySearchCondition)

@given(instance=query::QuerySearchCondition_strategy)
def test_query::querysearchcondition_negatedCondition_type(instance):
    assert isinstance(instance.negatedCondition, bool)


@given(instance=query::QuerySearchCondition_strategy)
def test_query::querysearchcondition_negatedCondition_setter(instance):
    original = instance.negatedCondition
    instance.negatedCondition = original
    assert instance.negatedCondition == original

@given(instance=query::WithTableSpecification_strategy)
@settings(max_examples=50)
def test_query::withtablespecification_instantiation(instance):
    assert isinstance(instance, query::WithTableSpecification)

@given(instance=query::ValueExpressionCaseSearchContent_strategy)
@settings(max_examples=50)
def test_query::valueexpressioncasesearchcontent_instantiation(instance):
    assert isinstance(instance, query::ValueExpressionCaseSearchContent)

@given(instance=query::TableReference_strategy)
@settings(max_examples=50)
def test_query::tablereference_instantiation(instance):
    assert isinstance(instance, query::TableReference)

@given(instance=query::UpdateSource_strategy)
@settings(max_examples=50)
def test_query::updatesource_instantiation(instance):
    assert isinstance(instance, query::UpdateSource)

@given(instance=query::CursorReference_strategy)
@settings(max_examples=50)
def test_query::cursorreference_instantiation(instance):
    assert isinstance(instance, query::CursorReference)

@given(instance=query::MergeSourceTable_strategy)
@settings(max_examples=50)
def test_query::mergesourcetable_instantiation(instance):
    assert isinstance(instance, query::MergeSourceTable)

@given(instance=query::QueryValueExpression_strategy)
@settings(max_examples=50)
def test_query::queryvalueexpression_instantiation(instance):
    assert isinstance(instance, query::QueryValueExpression)

@given(instance=query::QueryValueExpression_strategy)
def test_query::queryvalueexpression_unaryOperator_type(instance):
    assert isinstance(instance.unaryOperator, str)


@given(instance=query::QueryValueExpression_strategy)
def test_query::queryvalueexpression_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original

@given(instance=query::OrderBySpecification_strategy)
@settings(max_examples=50)
def test_query::orderbyspecification_instantiation(instance):
    assert isinstance(instance, query::OrderBySpecification)

@given(instance=query::OrderBySpecification_strategy)
def test_query::orderbyspecification_descending_type(instance):
    assert isinstance(instance.descending, bool)


@given(instance=query::OrderBySpecification_strategy)
def test_query::orderbyspecification_descending_setter(instance):
    original = instance.descending
    instance.descending = original
    assert instance.descending == original

@given(instance=query::OrderBySpecification_strategy)
def test_query::orderbyspecification_NullOrderingOption_type(instance):
    assert isinstance(instance.NullOrderingOption, str)


@given(instance=query::OrderBySpecification_strategy)
def test_query::orderbyspecification_NullOrderingOption_setter(instance):
    original = instance.NullOrderingOption
    instance.NullOrderingOption = original
    assert instance.NullOrderingOption == original

@given(instance=query::OrderBySpecification_strategy)
def test_query::orderbyspecification_OrderingSpecOption_type(instance):
    assert isinstance(instance.OrderingSpecOption, str)


@given(instance=query::OrderBySpecification_strategy)
def test_query::orderbyspecification_OrderingSpecOption_setter(instance):
    original = instance.OrderingSpecOption
    instance.OrderingSpecOption = original
    assert instance.OrderingSpecOption == original

@given(instance=query::MergeTargetTable_strategy)
@settings(max_examples=50)
def test_query::mergetargettable_instantiation(instance):
    assert isinstance(instance, query::MergeTargetTable)

@given(instance=query::QueryStatement_strategy)
@settings(max_examples=50)
def test_query::querystatement_instantiation(instance):
    assert isinstance(instance, query::QueryStatement)

@given(instance=QueryChangeStatement_strategy)
@settings(max_examples=50)
def test_querychangestatement_instantiation(instance):
    assert isinstance(instance, QueryChangeStatement)

@given(instance=query::QueryMergeStatement_strategy)
@settings(max_examples=50)
def test_query::querymergestatement_instantiation(instance):
    assert isinstance(instance, query::QueryMergeStatement)

@given(instance=query::QueryUpdateStatement_strategy)
@settings(max_examples=50)
def test_query::queryupdatestatement_instantiation(instance):
    assert isinstance(instance, query::QueryUpdateStatement)

@given(instance=query::QueryInsertStatement_strategy)
@settings(max_examples=50)
def test_query::queryinsertstatement_instantiation(instance):
    assert isinstance(instance, query::QueryInsertStatement)

@given(instance=query::QueryDeleteStatement_strategy)
@settings(max_examples=50)
def test_query::querydeletestatement_instantiation(instance):
    assert isinstance(instance, query::QueryDeleteStatement)
