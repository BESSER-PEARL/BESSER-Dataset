import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statements_SQLControlStatement,
    Procedure,
    MergeOperationSpecification,
    UpdateSource,
    statements_SQLDataChangeStatement,
    SQLObject,
    query_SQLQueryObject,
    Table,
    ValueExpressionCase,
    query_ValueExpressionCaseSearch,
    Grouping,
    query_SuperGroup,
    SuperGroupElement,
    query_SuperGroupElementExpression,
    query_SuperGroupElementSublist,
    GroupingSetsElement,
    query_GroupingSetsElementSublist,
    query_GroupingSetsElementExpression,
    GroupingSpecification,
    query_Grouping,
    query_GroupingSets,
    QueryValueExpression,
    query_ValueExpressionAtomic,
    Function,
    query_MergeInsertSpecification,
    ValueExpressionAtomic,
    query_ValueExpressionNullValue,
    query_ValueExpressionCase,
    query_ValueExpressionDefaultValue,
    query_ValueExpressionSimple,
    PredicateQuantified,
    PredicateIn,
    Predicate,
    query_PredicateQuantified,
    query_PredicateIn,
    QueryResultSpecification,
    query_ValueExpressionVariable,
    OrderBySpecification,
    query_OrderByOrdinal,
    query_OrderByResultColumn,
    QuerySearchCondition,
    query_Predicate,
    query_ResultTableAllColumns,
    TableReference,
    query_TableExpression,
    query_TableNested,
    QueryExpressionBody,
    query_QueryValues,
    query_ValueExpressionScalarSelect,
    query_ValueExpressionRow,
    query_UpdateSourceExprList,
    expressions_QueryExpression,
    query_ValueExpressionCaseSimple,
    query_ValueExpressionNested,
    query_ValueExpressionLabeledDuration,
    query_ValueExpressionCombined,
    query_ValueExpressionFunction,
    query_ValueExpressionCast,
    query_GroupingExpression,
    query_PredicateQuantifiedValueSelect,
    query_PredicateQuantifiedRowSelect,
    query_PredicateInValueSelect,
    query_PredicateInValueRowSelect,
    query_PredicateInValueList,
    query_PredicateBetween,
    query_PredicateLike,
    query_PredicateBasic,
    query_ResultColumn,
    query_OrderByValueExpression,
    query_PredicateIsNull,
    query_QueryNested,
    query_UpdateSourceQuery,
    query_PredicateExists,
    DataType,
    expressions_ValueExpression,
    TableExpression,
    query_WithTableReference,
    query_TableFunction,
    query_TableQueryLateral,
    query_QueryExpressionBody,
    query_SearchConditionNested,
    query_QuerySelect,
    query_QueryCombined,
    query_SearchConditionCombined,
    query_TableJoined,
    expressions_SearchCondition,
    query_MergeUpdateSpecification,
    QueryStatement,
    query_QueryChangeStatement,
    query_QuerySelectStatement,
    query_ValueExpressionColumn,
    query_TableInDatabase,
    statements_SQLDataStatement,
    SQLQueryObject,
    query_WithTableSpecification,
    query_MergeOnCondition,
    query_UpdateAssignmentExpression,
    query_CursorReference,
    query_ValueExpressionCaseSimpleContent,
    query_OrderBySpecification,
    query_GroupingSpecification,
    query_MergeOperationSpecification,
    query_ValuesRow,
    query_ColumnName,
    query_TableCorrelation,
    query_QueryResultSpecification,
    query_CallStatement,
    query_QueryValueExpression,
    query_ValueExpressionCaseSearchContent,
    query_GroupingSetsElement,
    query_QuerySearchCondition,
    query_UpdateOfColumn,
    query_SuperGroupElement,
    query_QueryExpressionRoot,
    query_ValueExpressionCaseElse,
    query_ProcedureReference,
    query_UpdateSource,
    query_MergeSourceTable,
    query_MergeTargetTable,
    query_TableReference,
    query_UpdatabilityExpression,
    query_QueryStatement,
    QueryChangeStatement,
    query_QueryMergeStatement,
    query_QueryInsertStatement,
    query_QueryUpdateStatement,
    query_QueryDeleteStatement,
    SearchConditionCombinedOperator,
    TableJoinedOperator,
    OrderingSpecType,
    QueryCombinedOperator,
    ValueExpressionLabeledDurationType,
    PredicateQuantifiedType,
    PredicateComparisonOperator,
    UpdatabilityType,
    SuperGroupType,
    ValueExpressionUnaryOperator,
    ValueExpressionCombinedOperator,
    NullOrderingType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statements_sqlcontrolstatement_is_not_abstract():
    assert not inspect.isabstract(statements_SQLControlStatement)


def test_statements_sqlcontrolstatement_constructor_exists():
    assert callable(statements_SQLControlStatement.__init__)


def test_statements_sqlcontrolstatement_constructor_args():
    sig = inspect.signature(statements_SQLControlStatement.__init__)
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



def test_statements_sqldatachangestatement_is_not_abstract():
    assert not inspect.isabstract(statements_SQLDataChangeStatement)


def test_statements_sqldatachangestatement_constructor_exists():
    assert callable(statements_SQLDataChangeStatement.__init__)


def test_statements_sqldatachangestatement_constructor_args():
    sig = inspect.signature(statements_SQLDataChangeStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlobject_is_not_abstract():
    assert not inspect.isabstract(SQLObject)


def test_sqlobject_constructor_exists():
    assert callable(SQLObject.__init__)


def test_sqlobject_constructor_args():
    sig = inspect.signature(SQLObject.__init__)
    params = list(sig.parameters.keys())



def test_query_sqlqueryobject_is_not_abstract():
    assert not inspect.isabstract(query_SQLQueryObject)


def test_query_sqlqueryobject_constructor_exists():
    assert callable(query_SQLQueryObject.__init__)


def test_query_sqlqueryobject_constructor_args():
    sig = inspect.signature(query_SQLQueryObject.__init__)
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



def test_query_valueexpressioncasesearch_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionCaseSearch)


def test_query_valueexpressioncasesearch_constructor_exists():
    assert callable(query_ValueExpressionCaseSearch.__init__)


def test_query_valueexpressioncasesearch_constructor_args():
    sig = inspect.signature(query_ValueExpressionCaseSearch.__init__)
    params = list(sig.parameters.keys())



def test_grouping_is_not_abstract():
    assert not inspect.isabstract(Grouping)


def test_grouping_constructor_exists():
    assert callable(Grouping.__init__)


def test_grouping_constructor_args():
    sig = inspect.signature(Grouping.__init__)
    params = list(sig.parameters.keys())



def test_query_supergroup_is_not_abstract():
    assert not inspect.isabstract(query_SuperGroup)


def test_query_supergroup_constructor_exists():
    assert callable(query_SuperGroup.__init__)


def test_query_supergroup_constructor_args():
    sig = inspect.signature(query_SuperGroup.__init__)
    params = list(sig.parameters.keys())
    assert "superGroupType" in params, "Missing parameter 'superGroupType'"

def test_query_supergroup_has_superGroupType():
    assert hasattr(query_SuperGroup, "superGroupType")
    descriptor = None
    for klass in query_SuperGroup.__mro__:
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



def test_query_supergroupelementexpression_is_not_abstract():
    assert not inspect.isabstract(query_SuperGroupElementExpression)


def test_query_supergroupelementexpression_constructor_exists():
    assert callable(query_SuperGroupElementExpression.__init__)


def test_query_supergroupelementexpression_constructor_args():
    sig = inspect.signature(query_SuperGroupElementExpression.__init__)
    params = list(sig.parameters.keys())



def test_query_supergroupelementsublist_is_not_abstract():
    assert not inspect.isabstract(query_SuperGroupElementSublist)


def test_query_supergroupelementsublist_constructor_exists():
    assert callable(query_SuperGroupElementSublist.__init__)


def test_query_supergroupelementsublist_constructor_args():
    sig = inspect.signature(query_SuperGroupElementSublist.__init__)
    params = list(sig.parameters.keys())



def test_groupingsetselement_is_not_abstract():
    assert not inspect.isabstract(GroupingSetsElement)


def test_groupingsetselement_constructor_exists():
    assert callable(GroupingSetsElement.__init__)


def test_groupingsetselement_constructor_args():
    sig = inspect.signature(GroupingSetsElement.__init__)
    params = list(sig.parameters.keys())



def test_query_groupingsetselementsublist_is_not_abstract():
    assert not inspect.isabstract(query_GroupingSetsElementSublist)


def test_query_groupingsetselementsublist_constructor_exists():
    assert callable(query_GroupingSetsElementSublist.__init__)


def test_query_groupingsetselementsublist_constructor_args():
    sig = inspect.signature(query_GroupingSetsElementSublist.__init__)
    params = list(sig.parameters.keys())



def test_query_groupingsetselementexpression_is_not_abstract():
    assert not inspect.isabstract(query_GroupingSetsElementExpression)


def test_query_groupingsetselementexpression_constructor_exists():
    assert callable(query_GroupingSetsElementExpression.__init__)


def test_query_groupingsetselementexpression_constructor_args():
    sig = inspect.signature(query_GroupingSetsElementExpression.__init__)
    params = list(sig.parameters.keys())



def test_groupingspecification_is_not_abstract():
    assert not inspect.isabstract(GroupingSpecification)


def test_groupingspecification_constructor_exists():
    assert callable(GroupingSpecification.__init__)


def test_groupingspecification_constructor_args():
    sig = inspect.signature(GroupingSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query_grouping_is_not_abstract():
    assert not inspect.isabstract(query_Grouping)


def test_query_grouping_constructor_exists():
    assert callable(query_Grouping.__init__)


def test_query_grouping_constructor_args():
    sig = inspect.signature(query_Grouping.__init__)
    params = list(sig.parameters.keys())



def test_query_groupingsets_is_not_abstract():
    assert not inspect.isabstract(query_GroupingSets)


def test_query_groupingsets_constructor_exists():
    assert callable(query_GroupingSets.__init__)


def test_query_groupingsets_constructor_args():
    sig = inspect.signature(query_GroupingSets.__init__)
    params = list(sig.parameters.keys())



def test_queryvalueexpression_is_not_abstract():
    assert not inspect.isabstract(QueryValueExpression)


def test_queryvalueexpression_constructor_exists():
    assert callable(QueryValueExpression.__init__)


def test_queryvalueexpression_constructor_args():
    sig = inspect.signature(QueryValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressionatomic_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionAtomic)


def test_query_valueexpressionatomic_constructor_exists():
    assert callable(query_ValueExpressionAtomic.__init__)


def test_query_valueexpressionatomic_constructor_args():
    sig = inspect.signature(query_ValueExpressionAtomic.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_query_mergeinsertspecification_is_not_abstract():
    assert not inspect.isabstract(query_MergeInsertSpecification)


def test_query_mergeinsertspecification_constructor_exists():
    assert callable(query_MergeInsertSpecification.__init__)


def test_query_mergeinsertspecification_constructor_args():
    sig = inspect.signature(query_MergeInsertSpecification.__init__)
    params = list(sig.parameters.keys())



def test_valueexpressionatomic_is_not_abstract():
    assert not inspect.isabstract(ValueExpressionAtomic)


def test_valueexpressionatomic_constructor_exists():
    assert callable(ValueExpressionAtomic.__init__)


def test_valueexpressionatomic_constructor_args():
    sig = inspect.signature(ValueExpressionAtomic.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressionnullvalue_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionNullValue)


def test_query_valueexpressionnullvalue_constructor_exists():
    assert callable(query_ValueExpressionNullValue.__init__)


def test_query_valueexpressionnullvalue_constructor_args():
    sig = inspect.signature(query_ValueExpressionNullValue.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressioncase_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionCase)


def test_query_valueexpressioncase_constructor_exists():
    assert callable(query_ValueExpressionCase.__init__)


def test_query_valueexpressioncase_constructor_args():
    sig = inspect.signature(query_ValueExpressionCase.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressiondefaultvalue_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionDefaultValue)


def test_query_valueexpressiondefaultvalue_constructor_exists():
    assert callable(query_ValueExpressionDefaultValue.__init__)


def test_query_valueexpressiondefaultvalue_constructor_args():
    sig = inspect.signature(query_ValueExpressionDefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressionsimple_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionSimple)


def test_query_valueexpressionsimple_constructor_exists():
    assert callable(query_ValueExpressionSimple.__init__)


def test_query_valueexpressionsimple_constructor_args():
    sig = inspect.signature(query_ValueExpressionSimple.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_query_valueexpressionsimple_has_value():
    assert hasattr(query_ValueExpressionSimple, "value")
    descriptor = None
    for klass in query_ValueExpressionSimple.__mro__:
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



def test_query_predicatequantified_is_not_abstract():
    assert not inspect.isabstract(query_PredicateQuantified)


def test_query_predicatequantified_constructor_exists():
    assert callable(query_PredicateQuantified.__init__)


def test_query_predicatequantified_constructor_args():
    sig = inspect.signature(query_PredicateQuantified.__init__)
    params = list(sig.parameters.keys())



def test_query_predicatein_is_not_abstract():
    assert not inspect.isabstract(query_PredicateIn)


def test_query_predicatein_constructor_exists():
    assert callable(query_PredicateIn.__init__)


def test_query_predicatein_constructor_args():
    sig = inspect.signature(query_PredicateIn.__init__)
    params = list(sig.parameters.keys())
    assert "notIn" in params, "Missing parameter 'notIn'"

def test_query_predicatein_has_notIn():
    assert hasattr(query_PredicateIn, "notIn")
    descriptor = None
    for klass in query_PredicateIn.__mro__:
        if "notIn" in klass.__dict__:
            descriptor = klass.__dict__["notIn"]
            break
    assert isinstance(descriptor, property)



def test_queryresultspecification_is_not_abstract():
    assert not inspect.isabstract(QueryResultSpecification)


def test_queryresultspecification_constructor_exists():
    assert callable(QueryResultSpecification.__init__)


def test_queryresultspecification_constructor_args():
    sig = inspect.signature(QueryResultSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressionvariable_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionVariable)


def test_query_valueexpressionvariable_constructor_exists():
    assert callable(query_ValueExpressionVariable.__init__)


def test_query_valueexpressionvariable_constructor_args():
    sig = inspect.signature(query_ValueExpressionVariable.__init__)
    params = list(sig.parameters.keys())



def test_orderbyspecification_is_not_abstract():
    assert not inspect.isabstract(OrderBySpecification)


def test_orderbyspecification_constructor_exists():
    assert callable(OrderBySpecification.__init__)


def test_orderbyspecification_constructor_args():
    sig = inspect.signature(OrderBySpecification.__init__)
    params = list(sig.parameters.keys())



def test_query_orderbyordinal_is_not_abstract():
    assert not inspect.isabstract(query_OrderByOrdinal)


def test_query_orderbyordinal_constructor_exists():
    assert callable(query_OrderByOrdinal.__init__)


def test_query_orderbyordinal_constructor_args():
    sig = inspect.signature(query_OrderByOrdinal.__init__)
    params = list(sig.parameters.keys())
    assert "ordinalValue" in params, "Missing parameter 'ordinalValue'"

def test_query_orderbyordinal_has_ordinalValue():
    assert hasattr(query_OrderByOrdinal, "ordinalValue")
    descriptor = None
    for klass in query_OrderByOrdinal.__mro__:
        if "ordinalValue" in klass.__dict__:
            descriptor = klass.__dict__["ordinalValue"]
            break
    assert isinstance(descriptor, property)



def test_query_orderbyresultcolumn_is_not_abstract():
    assert not inspect.isabstract(query_OrderByResultColumn)


def test_query_orderbyresultcolumn_constructor_exists():
    assert callable(query_OrderByResultColumn.__init__)


def test_query_orderbyresultcolumn_constructor_args():
    sig = inspect.signature(query_OrderByResultColumn.__init__)
    params = list(sig.parameters.keys())



def test_querysearchcondition_is_not_abstract():
    assert not inspect.isabstract(QuerySearchCondition)


def test_querysearchcondition_constructor_exists():
    assert callable(QuerySearchCondition.__init__)


def test_querysearchcondition_constructor_args():
    sig = inspect.signature(QuerySearchCondition.__init__)
    params = list(sig.parameters.keys())



def test_query_predicate_is_not_abstract():
    assert not inspect.isabstract(query_Predicate)


def test_query_predicate_constructor_exists():
    assert callable(query_Predicate.__init__)


def test_query_predicate_constructor_args():
    sig = inspect.signature(query_Predicate.__init__)
    params = list(sig.parameters.keys())
    assert "negatedPredicate" in params, "Missing parameter 'negatedPredicate'"
    assert "selectivityValue" in params, "Missing parameter 'selectivityValue'"
    assert "hasSelectivity" in params, "Missing parameter 'hasSelectivity'"

def test_query_predicate_has_negatedPredicate():
    assert hasattr(query_Predicate, "negatedPredicate")
    descriptor = None
    for klass in query_Predicate.__mro__:
        if "negatedPredicate" in klass.__dict__:
            descriptor = klass.__dict__["negatedPredicate"]
            break
    assert isinstance(descriptor, property)

def test_query_predicate_has_selectivityValue():
    assert hasattr(query_Predicate, "selectivityValue")
    descriptor = None
    for klass in query_Predicate.__mro__:
        if "selectivityValue" in klass.__dict__:
            descriptor = klass.__dict__["selectivityValue"]
            break
    assert isinstance(descriptor, property)

def test_query_predicate_has_hasSelectivity():
    assert hasattr(query_Predicate, "hasSelectivity")
    descriptor = None
    for klass in query_Predicate.__mro__:
        if "hasSelectivity" in klass.__dict__:
            descriptor = klass.__dict__["hasSelectivity"]
            break
    assert isinstance(descriptor, property)



def test_query_resulttableallcolumns_is_not_abstract():
    assert not inspect.isabstract(query_ResultTableAllColumns)


def test_query_resulttableallcolumns_constructor_exists():
    assert callable(query_ResultTableAllColumns.__init__)


def test_query_resulttableallcolumns_constructor_args():
    sig = inspect.signature(query_ResultTableAllColumns.__init__)
    params = list(sig.parameters.keys())



def test_tablereference_is_not_abstract():
    assert not inspect.isabstract(TableReference)


def test_tablereference_constructor_exists():
    assert callable(TableReference.__init__)


def test_tablereference_constructor_args():
    sig = inspect.signature(TableReference.__init__)
    params = list(sig.parameters.keys())



def test_query_tableexpression_is_not_abstract():
    assert not inspect.isabstract(query_TableExpression)


def test_query_tableexpression_constructor_exists():
    assert callable(query_TableExpression.__init__)


def test_query_tableexpression_constructor_args():
    sig = inspect.signature(query_TableExpression.__init__)
    params = list(sig.parameters.keys())



def test_query_tablenested_is_not_abstract():
    assert not inspect.isabstract(query_TableNested)


def test_query_tablenested_constructor_exists():
    assert callable(query_TableNested.__init__)


def test_query_tablenested_constructor_args():
    sig = inspect.signature(query_TableNested.__init__)
    params = list(sig.parameters.keys())



def test_queryexpressionbody_is_not_abstract():
    assert not inspect.isabstract(QueryExpressionBody)


def test_queryexpressionbody_constructor_exists():
    assert callable(QueryExpressionBody.__init__)


def test_queryexpressionbody_constructor_args():
    sig = inspect.signature(QueryExpressionBody.__init__)
    params = list(sig.parameters.keys())



def test_query_queryvalues_is_not_abstract():
    assert not inspect.isabstract(query_QueryValues)


def test_query_queryvalues_constructor_exists():
    assert callable(query_QueryValues.__init__)


def test_query_queryvalues_constructor_args():
    sig = inspect.signature(query_QueryValues.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressionscalarselect_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionScalarSelect)


def test_query_valueexpressionscalarselect_constructor_exists():
    assert callable(query_ValueExpressionScalarSelect.__init__)


def test_query_valueexpressionscalarselect_constructor_args():
    sig = inspect.signature(query_ValueExpressionScalarSelect.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressionrow_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionRow)


def test_query_valueexpressionrow_constructor_exists():
    assert callable(query_ValueExpressionRow.__init__)


def test_query_valueexpressionrow_constructor_args():
    sig = inspect.signature(query_ValueExpressionRow.__init__)
    params = list(sig.parameters.keys())



def test_query_updatesourceexprlist_is_not_abstract():
    assert not inspect.isabstract(query_UpdateSourceExprList)


def test_query_updatesourceexprlist_constructor_exists():
    assert callable(query_UpdateSourceExprList.__init__)


def test_query_updatesourceexprlist_constructor_args():
    sig = inspect.signature(query_UpdateSourceExprList.__init__)
    params = list(sig.parameters.keys())



def test_expressions_queryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_QueryExpression)


def test_expressions_queryexpression_constructor_exists():
    assert callable(expressions_QueryExpression.__init__)


def test_expressions_queryexpression_constructor_args():
    sig = inspect.signature(expressions_QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressioncasesimple_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionCaseSimple)


def test_query_valueexpressioncasesimple_constructor_exists():
    assert callable(query_ValueExpressionCaseSimple.__init__)


def test_query_valueexpressioncasesimple_constructor_args():
    sig = inspect.signature(query_ValueExpressionCaseSimple.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressionnested_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionNested)


def test_query_valueexpressionnested_constructor_exists():
    assert callable(query_ValueExpressionNested.__init__)


def test_query_valueexpressionnested_constructor_args():
    sig = inspect.signature(query_ValueExpressionNested.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressionlabeledduration_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionLabeledDuration)


def test_query_valueexpressionlabeledduration_constructor_exists():
    assert callable(query_ValueExpressionLabeledDuration.__init__)


def test_query_valueexpressionlabeledduration_constructor_args():
    sig = inspect.signature(query_ValueExpressionLabeledDuration.__init__)
    params = list(sig.parameters.keys())
    assert "labeledDurationType" in params, "Missing parameter 'labeledDurationType'"

def test_query_valueexpressionlabeledduration_has_labeledDurationType():
    assert hasattr(query_ValueExpressionLabeledDuration, "labeledDurationType")
    descriptor = None
    for klass in query_ValueExpressionLabeledDuration.__mro__:
        if "labeledDurationType" in klass.__dict__:
            descriptor = klass.__dict__["labeledDurationType"]
            break
    assert isinstance(descriptor, property)



def test_query_valueexpressioncombined_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionCombined)


def test_query_valueexpressioncombined_constructor_exists():
    assert callable(query_ValueExpressionCombined.__init__)


def test_query_valueexpressioncombined_constructor_args():
    sig = inspect.signature(query_ValueExpressionCombined.__init__)
    params = list(sig.parameters.keys())
    assert "combinedOperator" in params, "Missing parameter 'combinedOperator'"

def test_query_valueexpressioncombined_has_combinedOperator():
    assert hasattr(query_ValueExpressionCombined, "combinedOperator")
    descriptor = None
    for klass in query_ValueExpressionCombined.__mro__:
        if "combinedOperator" in klass.__dict__:
            descriptor = klass.__dict__["combinedOperator"]
            break
    assert isinstance(descriptor, property)



def test_query_valueexpressionfunction_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionFunction)


def test_query_valueexpressionfunction_constructor_exists():
    assert callable(query_ValueExpressionFunction.__init__)


def test_query_valueexpressionfunction_constructor_args():
    sig = inspect.signature(query_ValueExpressionFunction.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"
    assert "columnFunction" in params, "Missing parameter 'columnFunction'"
    assert "specialRegister" in params, "Missing parameter 'specialRegister'"

def test_query_valueexpressionfunction_has_distinct():
    assert hasattr(query_ValueExpressionFunction, "distinct")
    descriptor = None
    for klass in query_ValueExpressionFunction.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)

def test_query_valueexpressionfunction_has_columnFunction():
    assert hasattr(query_ValueExpressionFunction, "columnFunction")
    descriptor = None
    for klass in query_ValueExpressionFunction.__mro__:
        if "columnFunction" in klass.__dict__:
            descriptor = klass.__dict__["columnFunction"]
            break
    assert isinstance(descriptor, property)

def test_query_valueexpressionfunction_has_specialRegister():
    assert hasattr(query_ValueExpressionFunction, "specialRegister")
    descriptor = None
    for klass in query_ValueExpressionFunction.__mro__:
        if "specialRegister" in klass.__dict__:
            descriptor = klass.__dict__["specialRegister"]
            break
    assert isinstance(descriptor, property)



def test_query_valueexpressioncast_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionCast)


def test_query_valueexpressioncast_constructor_exists():
    assert callable(query_ValueExpressionCast.__init__)


def test_query_valueexpressioncast_constructor_args():
    sig = inspect.signature(query_ValueExpressionCast.__init__)
    params = list(sig.parameters.keys())



def test_query_groupingexpression_is_not_abstract():
    assert not inspect.isabstract(query_GroupingExpression)


def test_query_groupingexpression_constructor_exists():
    assert callable(query_GroupingExpression.__init__)


def test_query_groupingexpression_constructor_args():
    sig = inspect.signature(query_GroupingExpression.__init__)
    params = list(sig.parameters.keys())



def test_query_predicatequantifiedvalueselect_is_not_abstract():
    assert not inspect.isabstract(query_PredicateQuantifiedValueSelect)


def test_query_predicatequantifiedvalueselect_constructor_exists():
    assert callable(query_PredicateQuantifiedValueSelect.__init__)


def test_query_predicatequantifiedvalueselect_constructor_args():
    sig = inspect.signature(query_PredicateQuantifiedValueSelect.__init__)
    params = list(sig.parameters.keys())
    assert "comparisonOperator" in params, "Missing parameter 'comparisonOperator'"
    assert "quantifiedType" in params, "Missing parameter 'quantifiedType'"

def test_query_predicatequantifiedvalueselect_has_comparisonOperator():
    assert hasattr(query_PredicateQuantifiedValueSelect, "comparisonOperator")
    descriptor = None
    for klass in query_PredicateQuantifiedValueSelect.__mro__:
        if "comparisonOperator" in klass.__dict__:
            descriptor = klass.__dict__["comparisonOperator"]
            break
    assert isinstance(descriptor, property)

def test_query_predicatequantifiedvalueselect_has_quantifiedType():
    assert hasattr(query_PredicateQuantifiedValueSelect, "quantifiedType")
    descriptor = None
    for klass in query_PredicateQuantifiedValueSelect.__mro__:
        if "quantifiedType" in klass.__dict__:
            descriptor = klass.__dict__["quantifiedType"]
            break
    assert isinstance(descriptor, property)



def test_query_predicatequantifiedrowselect_is_not_abstract():
    assert not inspect.isabstract(query_PredicateQuantifiedRowSelect)


def test_query_predicatequantifiedrowselect_constructor_exists():
    assert callable(query_PredicateQuantifiedRowSelect.__init__)


def test_query_predicatequantifiedrowselect_constructor_args():
    sig = inspect.signature(query_PredicateQuantifiedRowSelect.__init__)
    params = list(sig.parameters.keys())
    assert "quantifiedType" in params, "Missing parameter 'quantifiedType'"

def test_query_predicatequantifiedrowselect_has_quantifiedType():
    assert hasattr(query_PredicateQuantifiedRowSelect, "quantifiedType")
    descriptor = None
    for klass in query_PredicateQuantifiedRowSelect.__mro__:
        if "quantifiedType" in klass.__dict__:
            descriptor = klass.__dict__["quantifiedType"]
            break
    assert isinstance(descriptor, property)



def test_query_predicateinvalueselect_is_not_abstract():
    assert not inspect.isabstract(query_PredicateInValueSelect)


def test_query_predicateinvalueselect_constructor_exists():
    assert callable(query_PredicateInValueSelect.__init__)


def test_query_predicateinvalueselect_constructor_args():
    sig = inspect.signature(query_PredicateInValueSelect.__init__)
    params = list(sig.parameters.keys())



def test_query_predicateinvaluerowselect_is_not_abstract():
    assert not inspect.isabstract(query_PredicateInValueRowSelect)


def test_query_predicateinvaluerowselect_constructor_exists():
    assert callable(query_PredicateInValueRowSelect.__init__)


def test_query_predicateinvaluerowselect_constructor_args():
    sig = inspect.signature(query_PredicateInValueRowSelect.__init__)
    params = list(sig.parameters.keys())



def test_query_predicateinvaluelist_is_not_abstract():
    assert not inspect.isabstract(query_PredicateInValueList)


def test_query_predicateinvaluelist_constructor_exists():
    assert callable(query_PredicateInValueList.__init__)


def test_query_predicateinvaluelist_constructor_args():
    sig = inspect.signature(query_PredicateInValueList.__init__)
    params = list(sig.parameters.keys())



def test_query_predicatebetween_is_not_abstract():
    assert not inspect.isabstract(query_PredicateBetween)


def test_query_predicatebetween_constructor_exists():
    assert callable(query_PredicateBetween.__init__)


def test_query_predicatebetween_constructor_args():
    sig = inspect.signature(query_PredicateBetween.__init__)
    params = list(sig.parameters.keys())
    assert "notBetween" in params, "Missing parameter 'notBetween'"

def test_query_predicatebetween_has_notBetween():
    assert hasattr(query_PredicateBetween, "notBetween")
    descriptor = None
    for klass in query_PredicateBetween.__mro__:
        if "notBetween" in klass.__dict__:
            descriptor = klass.__dict__["notBetween"]
            break
    assert isinstance(descriptor, property)



def test_query_predicatelike_is_not_abstract():
    assert not inspect.isabstract(query_PredicateLike)


def test_query_predicatelike_constructor_exists():
    assert callable(query_PredicateLike.__init__)


def test_query_predicatelike_constructor_args():
    sig = inspect.signature(query_PredicateLike.__init__)
    params = list(sig.parameters.keys())
    assert "notLike" in params, "Missing parameter 'notLike'"

def test_query_predicatelike_has_notLike():
    assert hasattr(query_PredicateLike, "notLike")
    descriptor = None
    for klass in query_PredicateLike.__mro__:
        if "notLike" in klass.__dict__:
            descriptor = klass.__dict__["notLike"]
            break
    assert isinstance(descriptor, property)



def test_query_predicatebasic_is_not_abstract():
    assert not inspect.isabstract(query_PredicateBasic)


def test_query_predicatebasic_constructor_exists():
    assert callable(query_PredicateBasic.__init__)


def test_query_predicatebasic_constructor_args():
    sig = inspect.signature(query_PredicateBasic.__init__)
    params = list(sig.parameters.keys())
    assert "comparisonOperator" in params, "Missing parameter 'comparisonOperator'"

def test_query_predicatebasic_has_comparisonOperator():
    assert hasattr(query_PredicateBasic, "comparisonOperator")
    descriptor = None
    for klass in query_PredicateBasic.__mro__:
        if "comparisonOperator" in klass.__dict__:
            descriptor = klass.__dict__["comparisonOperator"]
            break
    assert isinstance(descriptor, property)



def test_query_resultcolumn_is_not_abstract():
    assert not inspect.isabstract(query_ResultColumn)


def test_query_resultcolumn_constructor_exists():
    assert callable(query_ResultColumn.__init__)


def test_query_resultcolumn_constructor_args():
    sig = inspect.signature(query_ResultColumn.__init__)
    params = list(sig.parameters.keys())



def test_query_orderbyvalueexpression_is_not_abstract():
    assert not inspect.isabstract(query_OrderByValueExpression)


def test_query_orderbyvalueexpression_constructor_exists():
    assert callable(query_OrderByValueExpression.__init__)


def test_query_orderbyvalueexpression_constructor_args():
    sig = inspect.signature(query_OrderByValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_query_predicateisnull_is_not_abstract():
    assert not inspect.isabstract(query_PredicateIsNull)


def test_query_predicateisnull_constructor_exists():
    assert callable(query_PredicateIsNull.__init__)


def test_query_predicateisnull_constructor_args():
    sig = inspect.signature(query_PredicateIsNull.__init__)
    params = list(sig.parameters.keys())
    assert "notNull" in params, "Missing parameter 'notNull'"

def test_query_predicateisnull_has_notNull():
    assert hasattr(query_PredicateIsNull, "notNull")
    descriptor = None
    for klass in query_PredicateIsNull.__mro__:
        if "notNull" in klass.__dict__:
            descriptor = klass.__dict__["notNull"]
            break
    assert isinstance(descriptor, property)



def test_query_querynested_is_not_abstract():
    assert not inspect.isabstract(query_QueryNested)


def test_query_querynested_constructor_exists():
    assert callable(query_QueryNested.__init__)


def test_query_querynested_constructor_args():
    sig = inspect.signature(query_QueryNested.__init__)
    params = list(sig.parameters.keys())



def test_query_updatesourcequery_is_not_abstract():
    assert not inspect.isabstract(query_UpdateSourceQuery)


def test_query_updatesourcequery_constructor_exists():
    assert callable(query_UpdateSourceQuery.__init__)


def test_query_updatesourcequery_constructor_args():
    sig = inspect.signature(query_UpdateSourceQuery.__init__)
    params = list(sig.parameters.keys())



def test_query_predicateexists_is_not_abstract():
    assert not inspect.isabstract(query_PredicateExists)


def test_query_predicateexists_constructor_exists():
    assert callable(query_PredicateExists.__init__)


def test_query_predicateexists_constructor_args():
    sig = inspect.signature(query_PredicateExists.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_expressions_valueexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ValueExpression)


def test_expressions_valueexpression_constructor_exists():
    assert callable(expressions_ValueExpression.__init__)


def test_expressions_valueexpression_constructor_args():
    sig = inspect.signature(expressions_ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_tableexpression_is_not_abstract():
    assert not inspect.isabstract(TableExpression)


def test_tableexpression_constructor_exists():
    assert callable(TableExpression.__init__)


def test_tableexpression_constructor_args():
    sig = inspect.signature(TableExpression.__init__)
    params = list(sig.parameters.keys())



def test_query_withtablereference_is_not_abstract():
    assert not inspect.isabstract(query_WithTableReference)


def test_query_withtablereference_constructor_exists():
    assert callable(query_WithTableReference.__init__)


def test_query_withtablereference_constructor_args():
    sig = inspect.signature(query_WithTableReference.__init__)
    params = list(sig.parameters.keys())



def test_query_tablefunction_is_not_abstract():
    assert not inspect.isabstract(query_TableFunction)


def test_query_tablefunction_constructor_exists():
    assert callable(query_TableFunction.__init__)


def test_query_tablefunction_constructor_args():
    sig = inspect.signature(query_TableFunction.__init__)
    params = list(sig.parameters.keys())



def test_query_tablequerylateral_is_not_abstract():
    assert not inspect.isabstract(query_TableQueryLateral)


def test_query_tablequerylateral_constructor_exists():
    assert callable(query_TableQueryLateral.__init__)


def test_query_tablequerylateral_constructor_args():
    sig = inspect.signature(query_TableQueryLateral.__init__)
    params = list(sig.parameters.keys())



def test_query_queryexpressionbody_is_not_abstract():
    assert not inspect.isabstract(query_QueryExpressionBody)


def test_query_queryexpressionbody_constructor_exists():
    assert callable(query_QueryExpressionBody.__init__)


def test_query_queryexpressionbody_constructor_args():
    sig = inspect.signature(query_QueryExpressionBody.__init__)
    params = list(sig.parameters.keys())
    assert "rowFetchLimit" in params, "Missing parameter 'rowFetchLimit'"

def test_query_queryexpressionbody_has_rowFetchLimit():
    assert hasattr(query_QueryExpressionBody, "rowFetchLimit")
    descriptor = None
    for klass in query_QueryExpressionBody.__mro__:
        if "rowFetchLimit" in klass.__dict__:
            descriptor = klass.__dict__["rowFetchLimit"]
            break
    assert isinstance(descriptor, property)



def test_query_searchconditionnested_is_not_abstract():
    assert not inspect.isabstract(query_SearchConditionNested)


def test_query_searchconditionnested_constructor_exists():
    assert callable(query_SearchConditionNested.__init__)


def test_query_searchconditionnested_constructor_args():
    sig = inspect.signature(query_SearchConditionNested.__init__)
    params = list(sig.parameters.keys())



def test_query_queryselect_is_not_abstract():
    assert not inspect.isabstract(query_QuerySelect)


def test_query_queryselect_constructor_exists():
    assert callable(query_QuerySelect.__init__)


def test_query_queryselect_constructor_args():
    sig = inspect.signature(query_QuerySelect.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_query_queryselect_has_distinct():
    assert hasattr(query_QuerySelect, "distinct")
    descriptor = None
    for klass in query_QuerySelect.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_query_querycombined_is_not_abstract():
    assert not inspect.isabstract(query_QueryCombined)


def test_query_querycombined_constructor_exists():
    assert callable(query_QueryCombined.__init__)


def test_query_querycombined_constructor_args():
    sig = inspect.signature(query_QueryCombined.__init__)
    params = list(sig.parameters.keys())
    assert "combinedOperator" in params, "Missing parameter 'combinedOperator'"

def test_query_querycombined_has_combinedOperator():
    assert hasattr(query_QueryCombined, "combinedOperator")
    descriptor = None
    for klass in query_QueryCombined.__mro__:
        if "combinedOperator" in klass.__dict__:
            descriptor = klass.__dict__["combinedOperator"]
            break
    assert isinstance(descriptor, property)



def test_query_searchconditioncombined_is_not_abstract():
    assert not inspect.isabstract(query_SearchConditionCombined)


def test_query_searchconditioncombined_constructor_exists():
    assert callable(query_SearchConditionCombined.__init__)


def test_query_searchconditioncombined_constructor_args():
    sig = inspect.signature(query_SearchConditionCombined.__init__)
    params = list(sig.parameters.keys())
    assert "combinedOperator" in params, "Missing parameter 'combinedOperator'"

def test_query_searchconditioncombined_has_combinedOperator():
    assert hasattr(query_SearchConditionCombined, "combinedOperator")
    descriptor = None
    for klass in query_SearchConditionCombined.__mro__:
        if "combinedOperator" in klass.__dict__:
            descriptor = klass.__dict__["combinedOperator"]
            break
    assert isinstance(descriptor, property)



def test_query_tablejoined_is_not_abstract():
    assert not inspect.isabstract(query_TableJoined)


def test_query_tablejoined_constructor_exists():
    assert callable(query_TableJoined.__init__)


def test_query_tablejoined_constructor_args():
    sig = inspect.signature(query_TableJoined.__init__)
    params = list(sig.parameters.keys())
    assert "joinOperator" in params, "Missing parameter 'joinOperator'"

def test_query_tablejoined_has_joinOperator():
    assert hasattr(query_TableJoined, "joinOperator")
    descriptor = None
    for klass in query_TableJoined.__mro__:
        if "joinOperator" in klass.__dict__:
            descriptor = klass.__dict__["joinOperator"]
            break
    assert isinstance(descriptor, property)



def test_expressions_searchcondition_is_not_abstract():
    assert not inspect.isabstract(expressions_SearchCondition)


def test_expressions_searchcondition_constructor_exists():
    assert callable(expressions_SearchCondition.__init__)


def test_expressions_searchcondition_constructor_args():
    sig = inspect.signature(expressions_SearchCondition.__init__)
    params = list(sig.parameters.keys())



def test_query_mergeupdatespecification_is_not_abstract():
    assert not inspect.isabstract(query_MergeUpdateSpecification)


def test_query_mergeupdatespecification_constructor_exists():
    assert callable(query_MergeUpdateSpecification.__init__)


def test_query_mergeupdatespecification_constructor_args():
    sig = inspect.signature(query_MergeUpdateSpecification.__init__)
    params = list(sig.parameters.keys())



def test_querystatement_is_not_abstract():
    assert not inspect.isabstract(QueryStatement)


def test_querystatement_constructor_exists():
    assert callable(QueryStatement.__init__)


def test_querystatement_constructor_args():
    sig = inspect.signature(QueryStatement.__init__)
    params = list(sig.parameters.keys())



def test_query_querychangestatement_is_not_abstract():
    assert not inspect.isabstract(query_QueryChangeStatement)


def test_query_querychangestatement_constructor_exists():
    assert callable(query_QueryChangeStatement.__init__)


def test_query_querychangestatement_constructor_args():
    sig = inspect.signature(query_QueryChangeStatement.__init__)
    params = list(sig.parameters.keys())



def test_query_queryselectstatement_is_not_abstract():
    assert not inspect.isabstract(query_QuerySelectStatement)


def test_query_queryselectstatement_constructor_exists():
    assert callable(query_QuerySelectStatement.__init__)


def test_query_queryselectstatement_constructor_args():
    sig = inspect.signature(query_QuerySelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressioncolumn_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionColumn)


def test_query_valueexpressioncolumn_constructor_exists():
    assert callable(query_ValueExpressionColumn.__init__)


def test_query_valueexpressioncolumn_constructor_args():
    sig = inspect.signature(query_ValueExpressionColumn.__init__)
    params = list(sig.parameters.keys())



def test_query_tableindatabase_is_not_abstract():
    assert not inspect.isabstract(query_TableInDatabase)


def test_query_tableindatabase_constructor_exists():
    assert callable(query_TableInDatabase.__init__)


def test_query_tableindatabase_constructor_args():
    sig = inspect.signature(query_TableInDatabase.__init__)
    params = list(sig.parameters.keys())



def test_statements_sqldatastatement_is_not_abstract():
    assert not inspect.isabstract(statements_SQLDataStatement)


def test_statements_sqldatastatement_constructor_exists():
    assert callable(statements_SQLDataStatement.__init__)


def test_statements_sqldatastatement_constructor_args():
    sig = inspect.signature(statements_SQLDataStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlqueryobject_is_not_abstract():
    assert not inspect.isabstract(SQLQueryObject)


def test_sqlqueryobject_constructor_exists():
    assert callable(SQLQueryObject.__init__)


def test_sqlqueryobject_constructor_args():
    sig = inspect.signature(SQLQueryObject.__init__)
    params = list(sig.parameters.keys())



def test_query_withtablespecification_is_not_abstract():
    assert not inspect.isabstract(query_WithTableSpecification)


def test_query_withtablespecification_constructor_exists():
    assert callable(query_WithTableSpecification.__init__)


def test_query_withtablespecification_constructor_args():
    sig = inspect.signature(query_WithTableSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query_mergeoncondition_is_not_abstract():
    assert not inspect.isabstract(query_MergeOnCondition)


def test_query_mergeoncondition_constructor_exists():
    assert callable(query_MergeOnCondition.__init__)


def test_query_mergeoncondition_constructor_args():
    sig = inspect.signature(query_MergeOnCondition.__init__)
    params = list(sig.parameters.keys())



def test_query_updateassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(query_UpdateAssignmentExpression)


def test_query_updateassignmentexpression_constructor_exists():
    assert callable(query_UpdateAssignmentExpression.__init__)


def test_query_updateassignmentexpression_constructor_args():
    sig = inspect.signature(query_UpdateAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_query_cursorreference_is_not_abstract():
    assert not inspect.isabstract(query_CursorReference)


def test_query_cursorreference_constructor_exists():
    assert callable(query_CursorReference.__init__)


def test_query_cursorreference_constructor_args():
    sig = inspect.signature(query_CursorReference.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressioncasesimplecontent_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionCaseSimpleContent)


def test_query_valueexpressioncasesimplecontent_constructor_exists():
    assert callable(query_ValueExpressionCaseSimpleContent.__init__)


def test_query_valueexpressioncasesimplecontent_constructor_args():
    sig = inspect.signature(query_ValueExpressionCaseSimpleContent.__init__)
    params = list(sig.parameters.keys())



def test_query_orderbyspecification_is_not_abstract():
    assert not inspect.isabstract(query_OrderBySpecification)


def test_query_orderbyspecification_constructor_exists():
    assert callable(query_OrderBySpecification.__init__)


def test_query_orderbyspecification_constructor_args():
    sig = inspect.signature(query_OrderBySpecification.__init__)
    params = list(sig.parameters.keys())
    assert "NullOrderingOption" in params, "Missing parameter 'NullOrderingOption'"
    assert "descending" in params, "Missing parameter 'descending'"
    assert "OrderingSpecOption" in params, "Missing parameter 'OrderingSpecOption'"

def test_query_orderbyspecification_has_NullOrderingOption():
    assert hasattr(query_OrderBySpecification, "NullOrderingOption")
    descriptor = None
    for klass in query_OrderBySpecification.__mro__:
        if "NullOrderingOption" in klass.__dict__:
            descriptor = klass.__dict__["NullOrderingOption"]
            break
    assert isinstance(descriptor, property)

def test_query_orderbyspecification_has_descending():
    assert hasattr(query_OrderBySpecification, "descending")
    descriptor = None
    for klass in query_OrderBySpecification.__mro__:
        if "descending" in klass.__dict__:
            descriptor = klass.__dict__["descending"]
            break
    assert isinstance(descriptor, property)

def test_query_orderbyspecification_has_OrderingSpecOption():
    assert hasattr(query_OrderBySpecification, "OrderingSpecOption")
    descriptor = None
    for klass in query_OrderBySpecification.__mro__:
        if "OrderingSpecOption" in klass.__dict__:
            descriptor = klass.__dict__["OrderingSpecOption"]
            break
    assert isinstance(descriptor, property)



def test_query_groupingspecification_is_not_abstract():
    assert not inspect.isabstract(query_GroupingSpecification)


def test_query_groupingspecification_constructor_exists():
    assert callable(query_GroupingSpecification.__init__)


def test_query_groupingspecification_constructor_args():
    sig = inspect.signature(query_GroupingSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query_mergeoperationspecification_is_not_abstract():
    assert not inspect.isabstract(query_MergeOperationSpecification)


def test_query_mergeoperationspecification_constructor_exists():
    assert callable(query_MergeOperationSpecification.__init__)


def test_query_mergeoperationspecification_constructor_args():
    sig = inspect.signature(query_MergeOperationSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query_valuesrow_is_not_abstract():
    assert not inspect.isabstract(query_ValuesRow)


def test_query_valuesrow_constructor_exists():
    assert callable(query_ValuesRow.__init__)


def test_query_valuesrow_constructor_args():
    sig = inspect.signature(query_ValuesRow.__init__)
    params = list(sig.parameters.keys())



def test_query_columnname_is_not_abstract():
    assert not inspect.isabstract(query_ColumnName)


def test_query_columnname_constructor_exists():
    assert callable(query_ColumnName.__init__)


def test_query_columnname_constructor_args():
    sig = inspect.signature(query_ColumnName.__init__)
    params = list(sig.parameters.keys())



def test_query_tablecorrelation_is_not_abstract():
    assert not inspect.isabstract(query_TableCorrelation)


def test_query_tablecorrelation_constructor_exists():
    assert callable(query_TableCorrelation.__init__)


def test_query_tablecorrelation_constructor_args():
    sig = inspect.signature(query_TableCorrelation.__init__)
    params = list(sig.parameters.keys())



def test_query_queryresultspecification_is_not_abstract():
    assert not inspect.isabstract(query_QueryResultSpecification)


def test_query_queryresultspecification_constructor_exists():
    assert callable(query_QueryResultSpecification.__init__)


def test_query_queryresultspecification_constructor_args():
    sig = inspect.signature(query_QueryResultSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query_callstatement_is_not_abstract():
    assert not inspect.isabstract(query_CallStatement)


def test_query_callstatement_constructor_exists():
    assert callable(query_CallStatement.__init__)


def test_query_callstatement_constructor_args():
    sig = inspect.signature(query_CallStatement.__init__)
    params = list(sig.parameters.keys())



def test_query_queryvalueexpression_is_not_abstract():
    assert not inspect.isabstract(query_QueryValueExpression)


def test_query_queryvalueexpression_constructor_exists():
    assert callable(query_QueryValueExpression.__init__)


def test_query_queryvalueexpression_constructor_args():
    sig = inspect.signature(query_QueryValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"

def test_query_queryvalueexpression_has_unaryOperator():
    assert hasattr(query_QueryValueExpression, "unaryOperator")
    descriptor = None
    for klass in query_QueryValueExpression.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_query_valueexpressioncasesearchcontent_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionCaseSearchContent)


def test_query_valueexpressioncasesearchcontent_constructor_exists():
    assert callable(query_ValueExpressionCaseSearchContent.__init__)


def test_query_valueexpressioncasesearchcontent_constructor_args():
    sig = inspect.signature(query_ValueExpressionCaseSearchContent.__init__)
    params = list(sig.parameters.keys())



def test_query_groupingsetselement_is_not_abstract():
    assert not inspect.isabstract(query_GroupingSetsElement)


def test_query_groupingsetselement_constructor_exists():
    assert callable(query_GroupingSetsElement.__init__)


def test_query_groupingsetselement_constructor_args():
    sig = inspect.signature(query_GroupingSetsElement.__init__)
    params = list(sig.parameters.keys())



def test_query_querysearchcondition_is_not_abstract():
    assert not inspect.isabstract(query_QuerySearchCondition)


def test_query_querysearchcondition_constructor_exists():
    assert callable(query_QuerySearchCondition.__init__)


def test_query_querysearchcondition_constructor_args():
    sig = inspect.signature(query_QuerySearchCondition.__init__)
    params = list(sig.parameters.keys())
    assert "negatedCondition" in params, "Missing parameter 'negatedCondition'"

def test_query_querysearchcondition_has_negatedCondition():
    assert hasattr(query_QuerySearchCondition, "negatedCondition")
    descriptor = None
    for klass in query_QuerySearchCondition.__mro__:
        if "negatedCondition" in klass.__dict__:
            descriptor = klass.__dict__["negatedCondition"]
            break
    assert isinstance(descriptor, property)



def test_query_updateofcolumn_is_not_abstract():
    assert not inspect.isabstract(query_UpdateOfColumn)


def test_query_updateofcolumn_constructor_exists():
    assert callable(query_UpdateOfColumn.__init__)


def test_query_updateofcolumn_constructor_args():
    sig = inspect.signature(query_UpdateOfColumn.__init__)
    params = list(sig.parameters.keys())



def test_query_supergroupelement_is_not_abstract():
    assert not inspect.isabstract(query_SuperGroupElement)


def test_query_supergroupelement_constructor_exists():
    assert callable(query_SuperGroupElement.__init__)


def test_query_supergroupelement_constructor_args():
    sig = inspect.signature(query_SuperGroupElement.__init__)
    params = list(sig.parameters.keys())



def test_query_queryexpressionroot_is_not_abstract():
    assert not inspect.isabstract(query_QueryExpressionRoot)


def test_query_queryexpressionroot_constructor_exists():
    assert callable(query_QueryExpressionRoot.__init__)


def test_query_queryexpressionroot_constructor_args():
    sig = inspect.signature(query_QueryExpressionRoot.__init__)
    params = list(sig.parameters.keys())



def test_query_valueexpressioncaseelse_is_not_abstract():
    assert not inspect.isabstract(query_ValueExpressionCaseElse)


def test_query_valueexpressioncaseelse_constructor_exists():
    assert callable(query_ValueExpressionCaseElse.__init__)


def test_query_valueexpressioncaseelse_constructor_args():
    sig = inspect.signature(query_ValueExpressionCaseElse.__init__)
    params = list(sig.parameters.keys())



def test_query_procedurereference_is_not_abstract():
    assert not inspect.isabstract(query_ProcedureReference)


def test_query_procedurereference_constructor_exists():
    assert callable(query_ProcedureReference.__init__)


def test_query_procedurereference_constructor_args():
    sig = inspect.signature(query_ProcedureReference.__init__)
    params = list(sig.parameters.keys())



def test_query_updatesource_is_not_abstract():
    assert not inspect.isabstract(query_UpdateSource)


def test_query_updatesource_constructor_exists():
    assert callable(query_UpdateSource.__init__)


def test_query_updatesource_constructor_args():
    sig = inspect.signature(query_UpdateSource.__init__)
    params = list(sig.parameters.keys())



def test_query_mergesourcetable_is_not_abstract():
    assert not inspect.isabstract(query_MergeSourceTable)


def test_query_mergesourcetable_constructor_exists():
    assert callable(query_MergeSourceTable.__init__)


def test_query_mergesourcetable_constructor_args():
    sig = inspect.signature(query_MergeSourceTable.__init__)
    params = list(sig.parameters.keys())



def test_query_mergetargettable_is_not_abstract():
    assert not inspect.isabstract(query_MergeTargetTable)


def test_query_mergetargettable_constructor_exists():
    assert callable(query_MergeTargetTable.__init__)


def test_query_mergetargettable_constructor_args():
    sig = inspect.signature(query_MergeTargetTable.__init__)
    params = list(sig.parameters.keys())



def test_query_tablereference_is_not_abstract():
    assert not inspect.isabstract(query_TableReference)


def test_query_tablereference_constructor_exists():
    assert callable(query_TableReference.__init__)


def test_query_tablereference_constructor_args():
    sig = inspect.signature(query_TableReference.__init__)
    params = list(sig.parameters.keys())



def test_query_updatabilityexpression_is_not_abstract():
    assert not inspect.isabstract(query_UpdatabilityExpression)


def test_query_updatabilityexpression_constructor_exists():
    assert callable(query_UpdatabilityExpression.__init__)


def test_query_updatabilityexpression_constructor_args():
    sig = inspect.signature(query_UpdatabilityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "updatabilityType" in params, "Missing parameter 'updatabilityType'"

def test_query_updatabilityexpression_has_updatabilityType():
    assert hasattr(query_UpdatabilityExpression, "updatabilityType")
    descriptor = None
    for klass in query_UpdatabilityExpression.__mro__:
        if "updatabilityType" in klass.__dict__:
            descriptor = klass.__dict__["updatabilityType"]
            break
    assert isinstance(descriptor, property)



def test_query_querystatement_is_not_abstract():
    assert not inspect.isabstract(query_QueryStatement)


def test_query_querystatement_constructor_exists():
    assert callable(query_QueryStatement.__init__)


def test_query_querystatement_constructor_args():
    sig = inspect.signature(query_QueryStatement.__init__)
    params = list(sig.parameters.keys())



def test_querychangestatement_is_not_abstract():
    assert not inspect.isabstract(QueryChangeStatement)


def test_querychangestatement_constructor_exists():
    assert callable(QueryChangeStatement.__init__)


def test_querychangestatement_constructor_args():
    sig = inspect.signature(QueryChangeStatement.__init__)
    params = list(sig.parameters.keys())



def test_query_querymergestatement_is_not_abstract():
    assert not inspect.isabstract(query_QueryMergeStatement)


def test_query_querymergestatement_constructor_exists():
    assert callable(query_QueryMergeStatement.__init__)


def test_query_querymergestatement_constructor_args():
    sig = inspect.signature(query_QueryMergeStatement.__init__)
    params = list(sig.parameters.keys())



def test_query_queryinsertstatement_is_not_abstract():
    assert not inspect.isabstract(query_QueryInsertStatement)


def test_query_queryinsertstatement_constructor_exists():
    assert callable(query_QueryInsertStatement.__init__)


def test_query_queryinsertstatement_constructor_args():
    sig = inspect.signature(query_QueryInsertStatement.__init__)
    params = list(sig.parameters.keys())



def test_query_queryupdatestatement_is_not_abstract():
    assert not inspect.isabstract(query_QueryUpdateStatement)


def test_query_queryupdatestatement_constructor_exists():
    assert callable(query_QueryUpdateStatement.__init__)


def test_query_queryupdatestatement_constructor_args():
    sig = inspect.signature(query_QueryUpdateStatement.__init__)
    params = list(sig.parameters.keys())



def test_query_querydeletestatement_is_not_abstract():
    assert not inspect.isabstract(query_QueryDeleteStatement)


def test_query_querydeletestatement_constructor_exists():
    assert callable(query_QueryDeleteStatement.__init__)


def test_query_querydeletestatement_constructor_args():
    sig = inspect.signature(query_QueryDeleteStatement.__init__)
    params = list(sig.parameters.keys())

def test_searchconditioncombinedoperator_exists():
    # Check that the Enumeration exists
    assert SearchConditionCombinedOperator is not None

def test_searchconditioncombinedoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SearchConditionCombinedOperator]
    expected_literals = [
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SearchConditionCombinedOperator"

def test_tablejoinedoperator_exists():
    # Check that the Enumeration exists
    assert TableJoinedOperator is not None

def test_tablejoinedoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TableJoinedOperator]
    expected_literals = [
        "EXPLICIT_INNER",
        "RIGHT_OUTER",
        "FULL_OUTER",
        "DEFAULT_INNER",
        "LEFT_OUTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TableJoinedOperator"

def test_orderingspectype_exists():
    # Check that the Enumeration exists
    assert OrderingSpecType is not None

def test_orderingspectype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderingSpecType]
    expected_literals = [
        "DESC",
        "ASC",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderingSpecType"

def test_querycombinedoperator_exists():
    # Check that the Enumeration exists
    assert QueryCombinedOperator is not None

def test_querycombinedoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QueryCombinedOperator]
    expected_literals = [
        "EXCEPT_ALL",
        "INTERSECT",
        "EXCEPT",
        "UNION",
        "UNION_ALL",
        "INTERSECT_ALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QueryCombinedOperator"

def test_valueexpressionlabeleddurationtype_exists():
    # Check that the Enumeration exists
    assert ValueExpressionLabeledDurationType is not None

def test_valueexpressionlabeleddurationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueExpressionLabeledDurationType]
    expected_literals = [
        "YEARS",
        "SECONDS",
        "MINUTES",
        "MICROSECONDS",
        "HOURS",
        "DAYS",
        "MONTHS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueExpressionLabeledDurationType"

def test_predicatequantifiedtype_exists():
    # Check that the Enumeration exists
    assert PredicateQuantifiedType is not None

def test_predicatequantifiedtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PredicateQuantifiedType]
    expected_literals = [
        "ALL",
        "ANY",
        "SOME",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PredicateQuantifiedType"

def test_predicatecomparisonoperator_exists():
    # Check that the Enumeration exists
    assert PredicateComparisonOperator is not None

def test_predicatecomparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PredicateComparisonOperator]
    expected_literals = [
        "GREATER_THAN_OR_EQUAL",
        "LESS_THAN",
        "GREATER_THAN",
        "NOT_EQUAL",
        "LESS_THAN_OR_EQUAL",
        "EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PredicateComparisonOperator"

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

def test_supergrouptype_exists():
    # Check that the Enumeration exists
    assert SuperGroupType is not None

def test_supergrouptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuperGroupType]
    expected_literals = [
        "GRANDTOTAL",
        "ROLLUP",
        "CUBE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SuperGroupType"

def test_valueexpressionunaryoperator_exists():
    # Check that the Enumeration exists
    assert ValueExpressionUnaryOperator is not None

def test_valueexpressionunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueExpressionUnaryOperator]
    expected_literals = [
        "NONE",
        "PLUS",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueExpressionUnaryOperator"

def test_valueexpressioncombinedoperator_exists():
    # Check that the Enumeration exists
    assert ValueExpressionCombinedOperator is not None

def test_valueexpressioncombinedoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueExpressionCombinedOperator]
    expected_literals = [
        "SUBTRACT",
        "DIVIDE",
        "ADD",
        "MULTIPLY",
        "CONCATENATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueExpressionCombinedOperator"

def test_nullorderingtype_exists():
    # Check that the Enumeration exists
    assert NullOrderingType is not None

def test_nullorderingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NullOrderingType]
    expected_literals = [
        "NULLS_FIRST",
        "NONE",
        "NULLS_LAST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NullOrderingType"


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
statements_SQLControlStatement_strategy = st.builds(
    statements_SQLControlStatement,
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
statements_SQLDataChangeStatement_strategy = st.builds(
    statements_SQLDataChangeStatement,
)
SQLObject_strategy = st.builds(
    SQLObject,
)
query_SQLQueryObject_strategy = st.builds(
    query_SQLQueryObject,
)
Table_strategy = st.builds(
    Table,
)
ValueExpressionCase_strategy = st.builds(
    ValueExpressionCase,
)
query_ValueExpressionCaseSearch_strategy = st.builds(
    query_ValueExpressionCaseSearch,
)
Grouping_strategy = st.builds(
    Grouping,
)
query_SuperGroup_strategy = st.builds(
    query_SuperGroup,
    superGroupType=
        safe_text
)
SuperGroupElement_strategy = st.builds(
    SuperGroupElement,
)
query_SuperGroupElementExpression_strategy = st.builds(
    query_SuperGroupElementExpression,
)
query_SuperGroupElementSublist_strategy = st.builds(
    query_SuperGroupElementSublist,
)
GroupingSetsElement_strategy = st.builds(
    GroupingSetsElement,
)
query_GroupingSetsElementSublist_strategy = st.builds(
    query_GroupingSetsElementSublist,
)
query_GroupingSetsElementExpression_strategy = st.builds(
    query_GroupingSetsElementExpression,
)
GroupingSpecification_strategy = st.builds(
    GroupingSpecification,
)
query_Grouping_strategy = st.builds(
    query_Grouping,
)
query_GroupingSets_strategy = st.builds(
    query_GroupingSets,
)
QueryValueExpression_strategy = st.builds(
    QueryValueExpression,
)
query_ValueExpressionAtomic_strategy = st.builds(
    query_ValueExpressionAtomic,
)
Function_strategy = st.builds(
    Function,
)
query_MergeInsertSpecification_strategy = st.builds(
    query_MergeInsertSpecification,
)
ValueExpressionAtomic_strategy = st.builds(
    ValueExpressionAtomic,
)
query_ValueExpressionNullValue_strategy = st.builds(
    query_ValueExpressionNullValue,
)
query_ValueExpressionCase_strategy = st.builds(
    query_ValueExpressionCase,
)
query_ValueExpressionDefaultValue_strategy = st.builds(
    query_ValueExpressionDefaultValue,
)
query_ValueExpressionSimple_strategy = st.builds(
    query_ValueExpressionSimple,
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
query_PredicateQuantified_strategy = st.builds(
    query_PredicateQuantified,
)
query_PredicateIn_strategy = st.builds(
    query_PredicateIn,
    notIn=
        st.booleans()
)
QueryResultSpecification_strategy = st.builds(
    QueryResultSpecification,
)
query_ValueExpressionVariable_strategy = st.builds(
    query_ValueExpressionVariable,
)
OrderBySpecification_strategy = st.builds(
    OrderBySpecification,
)
query_OrderByOrdinal_strategy = st.builds(
    query_OrderByOrdinal,
    ordinalValue=
        st.integers()
)
query_OrderByResultColumn_strategy = st.builds(
    query_OrderByResultColumn,
)
QuerySearchCondition_strategy = st.builds(
    QuerySearchCondition,
)
query_Predicate_strategy = st.builds(
    query_Predicate,
    negatedPredicate=
        st.booleans(),
    selectivityValue=
        safe_text,
    hasSelectivity=
        st.booleans()
)
query_ResultTableAllColumns_strategy = st.builds(
    query_ResultTableAllColumns,
)
TableReference_strategy = st.builds(
    TableReference,
)
query_TableExpression_strategy = st.builds(
    query_TableExpression,
)
query_TableNested_strategy = st.builds(
    query_TableNested,
)
QueryExpressionBody_strategy = st.builds(
    QueryExpressionBody,
)
query_QueryValues_strategy = st.builds(
    query_QueryValues,
)
query_ValueExpressionScalarSelect_strategy = st.builds(
    query_ValueExpressionScalarSelect,
)
query_ValueExpressionRow_strategy = st.builds(
    query_ValueExpressionRow,
)
query_UpdateSourceExprList_strategy = st.builds(
    query_UpdateSourceExprList,
)
expressions_QueryExpression_strategy = st.builds(
    expressions_QueryExpression,
)
query_ValueExpressionCaseSimple_strategy = st.builds(
    query_ValueExpressionCaseSimple,
)
query_ValueExpressionNested_strategy = st.builds(
    query_ValueExpressionNested,
)
query_ValueExpressionLabeledDuration_strategy = st.builds(
    query_ValueExpressionLabeledDuration,
    labeledDurationType=
        safe_text
)
query_ValueExpressionCombined_strategy = st.builds(
    query_ValueExpressionCombined,
    combinedOperator=
        safe_text
)
query_ValueExpressionFunction_strategy = st.builds(
    query_ValueExpressionFunction,
    distinct=
        st.booleans(),
    columnFunction=
        st.booleans(),
    specialRegister=
        st.booleans()
)
query_ValueExpressionCast_strategy = st.builds(
    query_ValueExpressionCast,
)
query_GroupingExpression_strategy = st.builds(
    query_GroupingExpression,
)
query_PredicateQuantifiedValueSelect_strategy = st.builds(
    query_PredicateQuantifiedValueSelect,
    comparisonOperator=
        safe_text,
    quantifiedType=
        safe_text
)
query_PredicateQuantifiedRowSelect_strategy = st.builds(
    query_PredicateQuantifiedRowSelect,
    quantifiedType=
        safe_text
)
query_PredicateInValueSelect_strategy = st.builds(
    query_PredicateInValueSelect,
)
query_PredicateInValueRowSelect_strategy = st.builds(
    query_PredicateInValueRowSelect,
)
query_PredicateInValueList_strategy = st.builds(
    query_PredicateInValueList,
)
query_PredicateBetween_strategy = st.builds(
    query_PredicateBetween,
    notBetween=
        st.booleans()
)
query_PredicateLike_strategy = st.builds(
    query_PredicateLike,
    notLike=
        st.booleans()
)
query_PredicateBasic_strategy = st.builds(
    query_PredicateBasic,
    comparisonOperator=
        safe_text
)
query_ResultColumn_strategy = st.builds(
    query_ResultColumn,
)
query_OrderByValueExpression_strategy = st.builds(
    query_OrderByValueExpression,
)
query_PredicateIsNull_strategy = st.builds(
    query_PredicateIsNull,
    notNull=
        st.booleans()
)
query_QueryNested_strategy = st.builds(
    query_QueryNested,
)
query_UpdateSourceQuery_strategy = st.builds(
    query_UpdateSourceQuery,
)
query_PredicateExists_strategy = st.builds(
    query_PredicateExists,
)
DataType_strategy = st.builds(
    DataType,
)
expressions_ValueExpression_strategy = st.builds(
    expressions_ValueExpression,
)
TableExpression_strategy = st.builds(
    TableExpression,
)
query_WithTableReference_strategy = st.builds(
    query_WithTableReference,
)
query_TableFunction_strategy = st.builds(
    query_TableFunction,
)
query_TableQueryLateral_strategy = st.builds(
    query_TableQueryLateral,
)
query_QueryExpressionBody_strategy = st.builds(
    query_QueryExpressionBody,
    rowFetchLimit=
        st.integers()
)
query_SearchConditionNested_strategy = st.builds(
    query_SearchConditionNested,
)
query_QuerySelect_strategy = st.builds(
    query_QuerySelect,
    distinct=
        st.booleans()
)
query_QueryCombined_strategy = st.builds(
    query_QueryCombined,
    combinedOperator=
        safe_text
)
query_SearchConditionCombined_strategy = st.builds(
    query_SearchConditionCombined,
    combinedOperator=
        safe_text
)
query_TableJoined_strategy = st.builds(
    query_TableJoined,
    joinOperator=
        safe_text
)
expressions_SearchCondition_strategy = st.builds(
    expressions_SearchCondition,
)
query_MergeUpdateSpecification_strategy = st.builds(
    query_MergeUpdateSpecification,
)
QueryStatement_strategy = st.builds(
    QueryStatement,
)
query_QueryChangeStatement_strategy = st.builds(
    query_QueryChangeStatement,
)
query_QuerySelectStatement_strategy = st.builds(
    query_QuerySelectStatement,
)
query_ValueExpressionColumn_strategy = st.builds(
    query_ValueExpressionColumn,
)
query_TableInDatabase_strategy = st.builds(
    query_TableInDatabase,
)
statements_SQLDataStatement_strategy = st.builds(
    statements_SQLDataStatement,
)
SQLQueryObject_strategy = st.builds(
    SQLQueryObject,
)
query_WithTableSpecification_strategy = st.builds(
    query_WithTableSpecification,
)
query_MergeOnCondition_strategy = st.builds(
    query_MergeOnCondition,
)
query_UpdateAssignmentExpression_strategy = st.builds(
    query_UpdateAssignmentExpression,
)
query_CursorReference_strategy = st.builds(
    query_CursorReference,
)
query_ValueExpressionCaseSimpleContent_strategy = st.builds(
    query_ValueExpressionCaseSimpleContent,
)
query_OrderBySpecification_strategy = st.builds(
    query_OrderBySpecification,
    NullOrderingOption=
        safe_text,
    descending=
        st.booleans(),
    OrderingSpecOption=
        safe_text
)
query_GroupingSpecification_strategy = st.builds(
    query_GroupingSpecification,
)
query_MergeOperationSpecification_strategy = st.builds(
    query_MergeOperationSpecification,
)
query_ValuesRow_strategy = st.builds(
    query_ValuesRow,
)
query_ColumnName_strategy = st.builds(
    query_ColumnName,
)
query_TableCorrelation_strategy = st.builds(
    query_TableCorrelation,
)
query_QueryResultSpecification_strategy = st.builds(
    query_QueryResultSpecification,
)
query_CallStatement_strategy = st.builds(
    query_CallStatement,
)
query_QueryValueExpression_strategy = st.builds(
    query_QueryValueExpression,
    unaryOperator=
        safe_text
)
query_ValueExpressionCaseSearchContent_strategy = st.builds(
    query_ValueExpressionCaseSearchContent,
)
query_GroupingSetsElement_strategy = st.builds(
    query_GroupingSetsElement,
)
query_QuerySearchCondition_strategy = st.builds(
    query_QuerySearchCondition,
    negatedCondition=
        st.booleans()
)
query_UpdateOfColumn_strategy = st.builds(
    query_UpdateOfColumn,
)
query_SuperGroupElement_strategy = st.builds(
    query_SuperGroupElement,
)
query_QueryExpressionRoot_strategy = st.builds(
    query_QueryExpressionRoot,
)
query_ValueExpressionCaseElse_strategy = st.builds(
    query_ValueExpressionCaseElse,
)
query_ProcedureReference_strategy = st.builds(
    query_ProcedureReference,
)
query_UpdateSource_strategy = st.builds(
    query_UpdateSource,
)
query_MergeSourceTable_strategy = st.builds(
    query_MergeSourceTable,
)
query_MergeTargetTable_strategy = st.builds(
    query_MergeTargetTable,
)
query_TableReference_strategy = st.builds(
    query_TableReference,
)
query_UpdatabilityExpression_strategy = st.builds(
    query_UpdatabilityExpression,
    updatabilityType=
        safe_text
)
query_QueryStatement_strategy = st.builds(
    query_QueryStatement,
)
QueryChangeStatement_strategy = st.builds(
    QueryChangeStatement,
)
query_QueryMergeStatement_strategy = st.builds(
    query_QueryMergeStatement,
)
query_QueryInsertStatement_strategy = st.builds(
    query_QueryInsertStatement,
)
query_QueryUpdateStatement_strategy = st.builds(
    query_QueryUpdateStatement,
)
query_QueryDeleteStatement_strategy = st.builds(
    query_QueryDeleteStatement,
)

@given(instance=statements_SQLControlStatement_strategy)
@settings(max_examples=50)
def test_statements_sqlcontrolstatement_instantiation(instance):
    assert isinstance(instance, statements_SQLControlStatement)

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

@given(instance=statements_SQLDataChangeStatement_strategy)
@settings(max_examples=50)
def test_statements_sqldatachangestatement_instantiation(instance):
    assert isinstance(instance, statements_SQLDataChangeStatement)

@given(instance=SQLObject_strategy)
@settings(max_examples=50)
def test_sqlobject_instantiation(instance):
    assert isinstance(instance, SQLObject)

@given(instance=query_SQLQueryObject_strategy)
@settings(max_examples=50)
def test_query_sqlqueryobject_instantiation(instance):
    assert isinstance(instance, query_SQLQueryObject)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=query_SQLQueryObject_strategy)
@settings(max_examples=30)
def test_query_sqlqueryobject_setsql_changes_state(instance):
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
        assert has_statements, f"Function 'setSQL' in query_SQLQueryObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSQL' in query_SQLQueryObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSQL' in query_SQLQueryObject is not implemented or raised an error")

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=ValueExpressionCase_strategy)
@settings(max_examples=50)
def test_valueexpressioncase_instantiation(instance):
    assert isinstance(instance, ValueExpressionCase)

@given(instance=query_ValueExpressionCaseSearch_strategy)
@settings(max_examples=50)
def test_query_valueexpressioncasesearch_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionCaseSearch)

@given(instance=Grouping_strategy)
@settings(max_examples=50)
def test_grouping_instantiation(instance):
    assert isinstance(instance, Grouping)

@given(instance=query_SuperGroup_strategy)
@settings(max_examples=50)
def test_query_supergroup_instantiation(instance):
    assert isinstance(instance, query_SuperGroup)



@given(instance=query_SuperGroup_strategy)
def test_query_supergroup_superGroupType_setter(instance):
    original = instance.superGroupType
    instance.superGroupType = original
    assert instance.superGroupType == original

@given(instance=SuperGroupElement_strategy)
@settings(max_examples=50)
def test_supergroupelement_instantiation(instance):
    assert isinstance(instance, SuperGroupElement)

@given(instance=query_SuperGroupElementExpression_strategy)
@settings(max_examples=50)
def test_query_supergroupelementexpression_instantiation(instance):
    assert isinstance(instance, query_SuperGroupElementExpression)

@given(instance=query_SuperGroupElementSublist_strategy)
@settings(max_examples=50)
def test_query_supergroupelementsublist_instantiation(instance):
    assert isinstance(instance, query_SuperGroupElementSublist)

@given(instance=GroupingSetsElement_strategy)
@settings(max_examples=50)
def test_groupingsetselement_instantiation(instance):
    assert isinstance(instance, GroupingSetsElement)

@given(instance=query_GroupingSetsElementSublist_strategy)
@settings(max_examples=50)
def test_query_groupingsetselementsublist_instantiation(instance):
    assert isinstance(instance, query_GroupingSetsElementSublist)

@given(instance=query_GroupingSetsElementExpression_strategy)
@settings(max_examples=50)
def test_query_groupingsetselementexpression_instantiation(instance):
    assert isinstance(instance, query_GroupingSetsElementExpression)

@given(instance=GroupingSpecification_strategy)
@settings(max_examples=50)
def test_groupingspecification_instantiation(instance):
    assert isinstance(instance, GroupingSpecification)

@given(instance=query_Grouping_strategy)
@settings(max_examples=50)
def test_query_grouping_instantiation(instance):
    assert isinstance(instance, query_Grouping)

@given(instance=query_GroupingSets_strategy)
@settings(max_examples=50)
def test_query_groupingsets_instantiation(instance):
    assert isinstance(instance, query_GroupingSets)

@given(instance=QueryValueExpression_strategy)
@settings(max_examples=50)
def test_queryvalueexpression_instantiation(instance):
    assert isinstance(instance, QueryValueExpression)

@given(instance=query_ValueExpressionAtomic_strategy)
@settings(max_examples=50)
def test_query_valueexpressionatomic_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionAtomic)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=query_MergeInsertSpecification_strategy)
@settings(max_examples=50)
def test_query_mergeinsertspecification_instantiation(instance):
    assert isinstance(instance, query_MergeInsertSpecification)

@given(instance=ValueExpressionAtomic_strategy)
@settings(max_examples=50)
def test_valueexpressionatomic_instantiation(instance):
    assert isinstance(instance, ValueExpressionAtomic)

@given(instance=query_ValueExpressionNullValue_strategy)
@settings(max_examples=50)
def test_query_valueexpressionnullvalue_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionNullValue)

@given(instance=query_ValueExpressionCase_strategy)
@settings(max_examples=50)
def test_query_valueexpressioncase_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionCase)

@given(instance=query_ValueExpressionDefaultValue_strategy)
@settings(max_examples=50)
def test_query_valueexpressiondefaultvalue_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionDefaultValue)

@given(instance=query_ValueExpressionSimple_strategy)
@settings(max_examples=50)
def test_query_valueexpressionsimple_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionSimple)



@given(instance=query_ValueExpressionSimple_strategy)
def test_query_valueexpressionsimple_value_setter(instance):
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

@given(instance=query_PredicateQuantified_strategy)
@settings(max_examples=50)
def test_query_predicatequantified_instantiation(instance):
    assert isinstance(instance, query_PredicateQuantified)

@given(instance=query_PredicateIn_strategy)
@settings(max_examples=50)
def test_query_predicatein_instantiation(instance):
    assert isinstance(instance, query_PredicateIn)



@given(instance=query_PredicateIn_strategy)
def test_query_predicatein_notIn_setter(instance):
    original = instance.notIn
    instance.notIn = original
    assert instance.notIn == original

@given(instance=QueryResultSpecification_strategy)
@settings(max_examples=50)
def test_queryresultspecification_instantiation(instance):
    assert isinstance(instance, QueryResultSpecification)

@given(instance=query_ValueExpressionVariable_strategy)
@settings(max_examples=50)
def test_query_valueexpressionvariable_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionVariable)

@given(instance=OrderBySpecification_strategy)
@settings(max_examples=50)
def test_orderbyspecification_instantiation(instance):
    assert isinstance(instance, OrderBySpecification)

@given(instance=query_OrderByOrdinal_strategy)
@settings(max_examples=50)
def test_query_orderbyordinal_instantiation(instance):
    assert isinstance(instance, query_OrderByOrdinal)



@given(instance=query_OrderByOrdinal_strategy)
def test_query_orderbyordinal_ordinalValue_setter(instance):
    original = instance.ordinalValue
    instance.ordinalValue = original
    assert instance.ordinalValue == original

@given(instance=query_OrderByResultColumn_strategy)
@settings(max_examples=50)
def test_query_orderbyresultcolumn_instantiation(instance):
    assert isinstance(instance, query_OrderByResultColumn)

@given(instance=QuerySearchCondition_strategy)
@settings(max_examples=50)
def test_querysearchcondition_instantiation(instance):
    assert isinstance(instance, QuerySearchCondition)

@given(instance=query_Predicate_strategy)
@settings(max_examples=50)
def test_query_predicate_instantiation(instance):
    assert isinstance(instance, query_Predicate)



@given(instance=query_Predicate_strategy)
def test_query_predicate_negatedPredicate_setter(instance):
    original = instance.negatedPredicate
    instance.negatedPredicate = original
    assert instance.negatedPredicate == original



@given(instance=query_Predicate_strategy)
def test_query_predicate_selectivityValue_setter(instance):
    original = instance.selectivityValue
    instance.selectivityValue = original
    assert instance.selectivityValue == original



@given(instance=query_Predicate_strategy)
def test_query_predicate_hasSelectivity_setter(instance):
    original = instance.hasSelectivity
    instance.hasSelectivity = original
    assert instance.hasSelectivity == original

@given(instance=query_ResultTableAllColumns_strategy)
@settings(max_examples=50)
def test_query_resulttableallcolumns_instantiation(instance):
    assert isinstance(instance, query_ResultTableAllColumns)

@given(instance=TableReference_strategy)
@settings(max_examples=50)
def test_tablereference_instantiation(instance):
    assert isinstance(instance, TableReference)

@given(instance=query_TableExpression_strategy)
@settings(max_examples=50)
def test_query_tableexpression_instantiation(instance):
    assert isinstance(instance, query_TableExpression)

@given(instance=query_TableNested_strategy)
@settings(max_examples=50)
def test_query_tablenested_instantiation(instance):
    assert isinstance(instance, query_TableNested)

@given(instance=QueryExpressionBody_strategy)
@settings(max_examples=50)
def test_queryexpressionbody_instantiation(instance):
    assert isinstance(instance, QueryExpressionBody)

@given(instance=query_QueryValues_strategy)
@settings(max_examples=50)
def test_query_queryvalues_instantiation(instance):
    assert isinstance(instance, query_QueryValues)

@given(instance=query_ValueExpressionScalarSelect_strategy)
@settings(max_examples=50)
def test_query_valueexpressionscalarselect_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionScalarSelect)

@given(instance=query_ValueExpressionRow_strategy)
@settings(max_examples=50)
def test_query_valueexpressionrow_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionRow)

@given(instance=query_UpdateSourceExprList_strategy)
@settings(max_examples=50)
def test_query_updatesourceexprlist_instantiation(instance):
    assert isinstance(instance, query_UpdateSourceExprList)

@given(instance=expressions_QueryExpression_strategy)
@settings(max_examples=50)
def test_expressions_queryexpression_instantiation(instance):
    assert isinstance(instance, expressions_QueryExpression)

@given(instance=query_ValueExpressionCaseSimple_strategy)
@settings(max_examples=50)
def test_query_valueexpressioncasesimple_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionCaseSimple)

@given(instance=query_ValueExpressionNested_strategy)
@settings(max_examples=50)
def test_query_valueexpressionnested_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionNested)

@given(instance=query_ValueExpressionLabeledDuration_strategy)
@settings(max_examples=50)
def test_query_valueexpressionlabeledduration_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionLabeledDuration)



@given(instance=query_ValueExpressionLabeledDuration_strategy)
def test_query_valueexpressionlabeledduration_labeledDurationType_setter(instance):
    original = instance.labeledDurationType
    instance.labeledDurationType = original
    assert instance.labeledDurationType == original

@given(instance=query_ValueExpressionCombined_strategy)
@settings(max_examples=50)
def test_query_valueexpressioncombined_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionCombined)



@given(instance=query_ValueExpressionCombined_strategy)
def test_query_valueexpressioncombined_combinedOperator_setter(instance):
    original = instance.combinedOperator
    instance.combinedOperator = original
    assert instance.combinedOperator == original

@given(instance=query_ValueExpressionFunction_strategy)
@settings(max_examples=50)
def test_query_valueexpressionfunction_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionFunction)



@given(instance=query_ValueExpressionFunction_strategy)
def test_query_valueexpressionfunction_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original



@given(instance=query_ValueExpressionFunction_strategy)
def test_query_valueexpressionfunction_columnFunction_setter(instance):
    original = instance.columnFunction
    instance.columnFunction = original
    assert instance.columnFunction == original



@given(instance=query_ValueExpressionFunction_strategy)
def test_query_valueexpressionfunction_specialRegister_setter(instance):
    original = instance.specialRegister
    instance.specialRegister = original
    assert instance.specialRegister == original

@given(instance=query_ValueExpressionCast_strategy)
@settings(max_examples=50)
def test_query_valueexpressioncast_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionCast)

@given(instance=query_GroupingExpression_strategy)
@settings(max_examples=50)
def test_query_groupingexpression_instantiation(instance):
    assert isinstance(instance, query_GroupingExpression)

@given(instance=query_PredicateQuantifiedValueSelect_strategy)
@settings(max_examples=50)
def test_query_predicatequantifiedvalueselect_instantiation(instance):
    assert isinstance(instance, query_PredicateQuantifiedValueSelect)



@given(instance=query_PredicateQuantifiedValueSelect_strategy)
def test_query_predicatequantifiedvalueselect_comparisonOperator_setter(instance):
    original = instance.comparisonOperator
    instance.comparisonOperator = original
    assert instance.comparisonOperator == original



@given(instance=query_PredicateQuantifiedValueSelect_strategy)
def test_query_predicatequantifiedvalueselect_quantifiedType_setter(instance):
    original = instance.quantifiedType
    instance.quantifiedType = original
    assert instance.quantifiedType == original

@given(instance=query_PredicateQuantifiedRowSelect_strategy)
@settings(max_examples=50)
def test_query_predicatequantifiedrowselect_instantiation(instance):
    assert isinstance(instance, query_PredicateQuantifiedRowSelect)



@given(instance=query_PredicateQuantifiedRowSelect_strategy)
def test_query_predicatequantifiedrowselect_quantifiedType_setter(instance):
    original = instance.quantifiedType
    instance.quantifiedType = original
    assert instance.quantifiedType == original

@given(instance=query_PredicateInValueSelect_strategy)
@settings(max_examples=50)
def test_query_predicateinvalueselect_instantiation(instance):
    assert isinstance(instance, query_PredicateInValueSelect)

@given(instance=query_PredicateInValueRowSelect_strategy)
@settings(max_examples=50)
def test_query_predicateinvaluerowselect_instantiation(instance):
    assert isinstance(instance, query_PredicateInValueRowSelect)

@given(instance=query_PredicateInValueList_strategy)
@settings(max_examples=50)
def test_query_predicateinvaluelist_instantiation(instance):
    assert isinstance(instance, query_PredicateInValueList)

@given(instance=query_PredicateBetween_strategy)
@settings(max_examples=50)
def test_query_predicatebetween_instantiation(instance):
    assert isinstance(instance, query_PredicateBetween)



@given(instance=query_PredicateBetween_strategy)
def test_query_predicatebetween_notBetween_setter(instance):
    original = instance.notBetween
    instance.notBetween = original
    assert instance.notBetween == original

@given(instance=query_PredicateLike_strategy)
@settings(max_examples=50)
def test_query_predicatelike_instantiation(instance):
    assert isinstance(instance, query_PredicateLike)



@given(instance=query_PredicateLike_strategy)
def test_query_predicatelike_notLike_setter(instance):
    original = instance.notLike
    instance.notLike = original
    assert instance.notLike == original

@given(instance=query_PredicateBasic_strategy)
@settings(max_examples=50)
def test_query_predicatebasic_instantiation(instance):
    assert isinstance(instance, query_PredicateBasic)



@given(instance=query_PredicateBasic_strategy)
def test_query_predicatebasic_comparisonOperator_setter(instance):
    original = instance.comparisonOperator
    instance.comparisonOperator = original
    assert instance.comparisonOperator == original

@given(instance=query_ResultColumn_strategy)
@settings(max_examples=50)
def test_query_resultcolumn_instantiation(instance):
    assert isinstance(instance, query_ResultColumn)

@given(instance=query_OrderByValueExpression_strategy)
@settings(max_examples=50)
def test_query_orderbyvalueexpression_instantiation(instance):
    assert isinstance(instance, query_OrderByValueExpression)

@given(instance=query_PredicateIsNull_strategy)
@settings(max_examples=50)
def test_query_predicateisnull_instantiation(instance):
    assert isinstance(instance, query_PredicateIsNull)



@given(instance=query_PredicateIsNull_strategy)
def test_query_predicateisnull_notNull_setter(instance):
    original = instance.notNull
    instance.notNull = original
    assert instance.notNull == original

@given(instance=query_QueryNested_strategy)
@settings(max_examples=50)
def test_query_querynested_instantiation(instance):
    assert isinstance(instance, query_QueryNested)

@given(instance=query_UpdateSourceQuery_strategy)
@settings(max_examples=50)
def test_query_updatesourcequery_instantiation(instance):
    assert isinstance(instance, query_UpdateSourceQuery)

@given(instance=query_PredicateExists_strategy)
@settings(max_examples=50)
def test_query_predicateexists_instantiation(instance):
    assert isinstance(instance, query_PredicateExists)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=expressions_ValueExpression_strategy)
@settings(max_examples=50)
def test_expressions_valueexpression_instantiation(instance):
    assert isinstance(instance, expressions_ValueExpression)

@given(instance=TableExpression_strategy)
@settings(max_examples=50)
def test_tableexpression_instantiation(instance):
    assert isinstance(instance, TableExpression)

@given(instance=query_WithTableReference_strategy)
@settings(max_examples=50)
def test_query_withtablereference_instantiation(instance):
    assert isinstance(instance, query_WithTableReference)

@given(instance=query_TableFunction_strategy)
@settings(max_examples=50)
def test_query_tablefunction_instantiation(instance):
    assert isinstance(instance, query_TableFunction)

@given(instance=query_TableQueryLateral_strategy)
@settings(max_examples=50)
def test_query_tablequerylateral_instantiation(instance):
    assert isinstance(instance, query_TableQueryLateral)

@given(instance=query_QueryExpressionBody_strategy)
@settings(max_examples=50)
def test_query_queryexpressionbody_instantiation(instance):
    assert isinstance(instance, query_QueryExpressionBody)



@given(instance=query_QueryExpressionBody_strategy)
def test_query_queryexpressionbody_rowFetchLimit_setter(instance):
    original = instance.rowFetchLimit
    instance.rowFetchLimit = original
    assert instance.rowFetchLimit == original

@given(instance=query_SearchConditionNested_strategy)
@settings(max_examples=50)
def test_query_searchconditionnested_instantiation(instance):
    assert isinstance(instance, query_SearchConditionNested)

@given(instance=query_QuerySelect_strategy)
@settings(max_examples=50)
def test_query_queryselect_instantiation(instance):
    assert isinstance(instance, query_QuerySelect)



@given(instance=query_QuerySelect_strategy)
def test_query_queryselect_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=query_QueryCombined_strategy)
@settings(max_examples=50)
def test_query_querycombined_instantiation(instance):
    assert isinstance(instance, query_QueryCombined)



@given(instance=query_QueryCombined_strategy)
def test_query_querycombined_combinedOperator_setter(instance):
    original = instance.combinedOperator
    instance.combinedOperator = original
    assert instance.combinedOperator == original

@given(instance=query_SearchConditionCombined_strategy)
@settings(max_examples=50)
def test_query_searchconditioncombined_instantiation(instance):
    assert isinstance(instance, query_SearchConditionCombined)



@given(instance=query_SearchConditionCombined_strategy)
def test_query_searchconditioncombined_combinedOperator_setter(instance):
    original = instance.combinedOperator
    instance.combinedOperator = original
    assert instance.combinedOperator == original

@given(instance=query_TableJoined_strategy)
@settings(max_examples=50)
def test_query_tablejoined_instantiation(instance):
    assert isinstance(instance, query_TableJoined)



@given(instance=query_TableJoined_strategy)
def test_query_tablejoined_joinOperator_setter(instance):
    original = instance.joinOperator
    instance.joinOperator = original
    assert instance.joinOperator == original

@given(instance=expressions_SearchCondition_strategy)
@settings(max_examples=50)
def test_expressions_searchcondition_instantiation(instance):
    assert isinstance(instance, expressions_SearchCondition)

@given(instance=query_MergeUpdateSpecification_strategy)
@settings(max_examples=50)
def test_query_mergeupdatespecification_instantiation(instance):
    assert isinstance(instance, query_MergeUpdateSpecification)

@given(instance=QueryStatement_strategy)
@settings(max_examples=50)
def test_querystatement_instantiation(instance):
    assert isinstance(instance, QueryStatement)

@given(instance=query_QueryChangeStatement_strategy)
@settings(max_examples=50)
def test_query_querychangestatement_instantiation(instance):
    assert isinstance(instance, query_QueryChangeStatement)

@given(instance=query_QuerySelectStatement_strategy)
@settings(max_examples=50)
def test_query_queryselectstatement_instantiation(instance):
    assert isinstance(instance, query_QuerySelectStatement)

@given(instance=query_ValueExpressionColumn_strategy)
@settings(max_examples=50)
def test_query_valueexpressioncolumn_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionColumn)

@given(instance=query_TableInDatabase_strategy)
@settings(max_examples=50)
def test_query_tableindatabase_instantiation(instance):
    assert isinstance(instance, query_TableInDatabase)

@given(instance=statements_SQLDataStatement_strategy)
@settings(max_examples=50)
def test_statements_sqldatastatement_instantiation(instance):
    assert isinstance(instance, statements_SQLDataStatement)

@given(instance=SQLQueryObject_strategy)
@settings(max_examples=50)
def test_sqlqueryobject_instantiation(instance):
    assert isinstance(instance, SQLQueryObject)

@given(instance=query_WithTableSpecification_strategy)
@settings(max_examples=50)
def test_query_withtablespecification_instantiation(instance):
    assert isinstance(instance, query_WithTableSpecification)

@given(instance=query_MergeOnCondition_strategy)
@settings(max_examples=50)
def test_query_mergeoncondition_instantiation(instance):
    assert isinstance(instance, query_MergeOnCondition)

@given(instance=query_UpdateAssignmentExpression_strategy)
@settings(max_examples=50)
def test_query_updateassignmentexpression_instantiation(instance):
    assert isinstance(instance, query_UpdateAssignmentExpression)

@given(instance=query_CursorReference_strategy)
@settings(max_examples=50)
def test_query_cursorreference_instantiation(instance):
    assert isinstance(instance, query_CursorReference)

@given(instance=query_ValueExpressionCaseSimpleContent_strategy)
@settings(max_examples=50)
def test_query_valueexpressioncasesimplecontent_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionCaseSimpleContent)

@given(instance=query_OrderBySpecification_strategy)
@settings(max_examples=50)
def test_query_orderbyspecification_instantiation(instance):
    assert isinstance(instance, query_OrderBySpecification)



@given(instance=query_OrderBySpecification_strategy)
def test_query_orderbyspecification_NullOrderingOption_setter(instance):
    original = instance.NullOrderingOption
    instance.NullOrderingOption = original
    assert instance.NullOrderingOption == original



@given(instance=query_OrderBySpecification_strategy)
def test_query_orderbyspecification_descending_setter(instance):
    original = instance.descending
    instance.descending = original
    assert instance.descending == original



@given(instance=query_OrderBySpecification_strategy)
def test_query_orderbyspecification_OrderingSpecOption_setter(instance):
    original = instance.OrderingSpecOption
    instance.OrderingSpecOption = original
    assert instance.OrderingSpecOption == original

@given(instance=query_GroupingSpecification_strategy)
@settings(max_examples=50)
def test_query_groupingspecification_instantiation(instance):
    assert isinstance(instance, query_GroupingSpecification)

@given(instance=query_MergeOperationSpecification_strategy)
@settings(max_examples=50)
def test_query_mergeoperationspecification_instantiation(instance):
    assert isinstance(instance, query_MergeOperationSpecification)

@given(instance=query_ValuesRow_strategy)
@settings(max_examples=50)
def test_query_valuesrow_instantiation(instance):
    assert isinstance(instance, query_ValuesRow)

@given(instance=query_ColumnName_strategy)
@settings(max_examples=50)
def test_query_columnname_instantiation(instance):
    assert isinstance(instance, query_ColumnName)

@given(instance=query_TableCorrelation_strategy)
@settings(max_examples=50)
def test_query_tablecorrelation_instantiation(instance):
    assert isinstance(instance, query_TableCorrelation)

@given(instance=query_QueryResultSpecification_strategy)
@settings(max_examples=50)
def test_query_queryresultspecification_instantiation(instance):
    assert isinstance(instance, query_QueryResultSpecification)

@given(instance=query_CallStatement_strategy)
@settings(max_examples=50)
def test_query_callstatement_instantiation(instance):
    assert isinstance(instance, query_CallStatement)

@given(instance=query_QueryValueExpression_strategy)
@settings(max_examples=50)
def test_query_queryvalueexpression_instantiation(instance):
    assert isinstance(instance, query_QueryValueExpression)



@given(instance=query_QueryValueExpression_strategy)
def test_query_queryvalueexpression_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original

@given(instance=query_ValueExpressionCaseSearchContent_strategy)
@settings(max_examples=50)
def test_query_valueexpressioncasesearchcontent_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionCaseSearchContent)

@given(instance=query_GroupingSetsElement_strategy)
@settings(max_examples=50)
def test_query_groupingsetselement_instantiation(instance):
    assert isinstance(instance, query_GroupingSetsElement)

@given(instance=query_QuerySearchCondition_strategy)
@settings(max_examples=50)
def test_query_querysearchcondition_instantiation(instance):
    assert isinstance(instance, query_QuerySearchCondition)



@given(instance=query_QuerySearchCondition_strategy)
def test_query_querysearchcondition_negatedCondition_setter(instance):
    original = instance.negatedCondition
    instance.negatedCondition = original
    assert instance.negatedCondition == original

@given(instance=query_UpdateOfColumn_strategy)
@settings(max_examples=50)
def test_query_updateofcolumn_instantiation(instance):
    assert isinstance(instance, query_UpdateOfColumn)

@given(instance=query_SuperGroupElement_strategy)
@settings(max_examples=50)
def test_query_supergroupelement_instantiation(instance):
    assert isinstance(instance, query_SuperGroupElement)

@given(instance=query_QueryExpressionRoot_strategy)
@settings(max_examples=50)
def test_query_queryexpressionroot_instantiation(instance):
    assert isinstance(instance, query_QueryExpressionRoot)

@given(instance=query_ValueExpressionCaseElse_strategy)
@settings(max_examples=50)
def test_query_valueexpressioncaseelse_instantiation(instance):
    assert isinstance(instance, query_ValueExpressionCaseElse)

@given(instance=query_ProcedureReference_strategy)
@settings(max_examples=50)
def test_query_procedurereference_instantiation(instance):
    assert isinstance(instance, query_ProcedureReference)

@given(instance=query_UpdateSource_strategy)
@settings(max_examples=50)
def test_query_updatesource_instantiation(instance):
    assert isinstance(instance, query_UpdateSource)

@given(instance=query_MergeSourceTable_strategy)
@settings(max_examples=50)
def test_query_mergesourcetable_instantiation(instance):
    assert isinstance(instance, query_MergeSourceTable)

@given(instance=query_MergeTargetTable_strategy)
@settings(max_examples=50)
def test_query_mergetargettable_instantiation(instance):
    assert isinstance(instance, query_MergeTargetTable)

@given(instance=query_TableReference_strategy)
@settings(max_examples=50)
def test_query_tablereference_instantiation(instance):
    assert isinstance(instance, query_TableReference)

@given(instance=query_UpdatabilityExpression_strategy)
@settings(max_examples=50)
def test_query_updatabilityexpression_instantiation(instance):
    assert isinstance(instance, query_UpdatabilityExpression)



@given(instance=query_UpdatabilityExpression_strategy)
def test_query_updatabilityexpression_updatabilityType_setter(instance):
    original = instance.updatabilityType
    instance.updatabilityType = original
    assert instance.updatabilityType == original

@given(instance=query_QueryStatement_strategy)
@settings(max_examples=50)
def test_query_querystatement_instantiation(instance):
    assert isinstance(instance, query_QueryStatement)

@given(instance=QueryChangeStatement_strategy)
@settings(max_examples=50)
def test_querychangestatement_instantiation(instance):
    assert isinstance(instance, QueryChangeStatement)

@given(instance=query_QueryMergeStatement_strategy)
@settings(max_examples=50)
def test_query_querymergestatement_instantiation(instance):
    assert isinstance(instance, query_QueryMergeStatement)

@given(instance=query_QueryInsertStatement_strategy)
@settings(max_examples=50)
def test_query_queryinsertstatement_instantiation(instance):
    assert isinstance(instance, query_QueryInsertStatement)

@given(instance=query_QueryUpdateStatement_strategy)
@settings(max_examples=50)
def test_query_queryupdatestatement_instantiation(instance):
    assert isinstance(instance, query_QueryUpdateStatement)

@given(instance=query_QueryDeleteStatement_strategy)
@settings(max_examples=50)
def test_query_querydeletestatement_instantiation(instance):
    assert isinstance(instance, query_QueryDeleteStatement)
